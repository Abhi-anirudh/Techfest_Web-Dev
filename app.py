from flask import Flask, request, jsonify, send_file
import pandas as pd
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
def allocate_rooms(group_data, hostel_data):
    allocation = []
    group_data['Gender'] = group_data['Gender'].str.lower()
    hostel_data['Gender'] = hostel_data['Gender'].str.lower()

    print("Group Data:")
    print(group_data)

    print("Hostel Data:")
    print(hostel_data)

    # Process according to the gender of the first group in group_data
    first_group_gender = group_data.loc[0, 'Gender']
    print(f"Allocating based on gender of first group: {first_group_gender}")

    for _, group in group_data.iterrows():
        group_id = group['Group ID']
        members = group['Members']
        gender = group['Gender']

        print(f"Processing group {group_id} with {members} members of gender {gender}")

        allocated = False  # Flag to track if group has been successfully allocated
        remaining_members = members  # Track remaining members to allocate

        for _, room in hostel_data[hostel_data['Gender'] == gender].iterrows():
            if remaining_members <= 0:
                break
            
            if remaining_members <= room['Capacity']:
                allocation.append([group_id, room['Hostel Name'], room['Room Number'], remaining_members])
                hostel_data.loc[room.name, 'Capacity'] -= remaining_members
                print(f"Allocated group {group_id} to {room['Hostel Name']} - Room {room['Room Number']} with {remaining_members} members")
                allocated = True
                remaining_members = 0
            else:
                allocation.append([group_id, room['Hostel Name'], room['Room Number'], room['Capacity']])
                hostel_data.loc[room.name, 'Capacity'] = 0
                print(f"Allocated group {group_id} partially to {room['Hostel Name']} - Room {room['Room Number']} with {room['Capacity']} members")
                remaining_members -= room['Capacity']

        if not allocated:
            allocation.append([group_id, 'No hostel available', 'No room available', members])
            print(f"No suitable room available for group {group_id}. Allocating as 'No hostel available'")

    print("Allocation:")
    print(allocation)

    return pd.DataFrame(allocation, columns=['Group ID', 'Hostel Name', 'Room Number', 'Members Allocated'])

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload_file():
    if 'group_file' not in request.files or 'hostel_file' not in request.files:
        return jsonify({'error': 'No file part'})

    group_file = request.files['group_file']
    hostel_file = request.files['hostel_file']
    
    try:
        group_data = pd.read_csv(group_file)
        hostel_data = pd.read_csv(hostel_file)

        allocation = allocate_rooms(group_data, hostel_data)

        output_path = "C:/Users/aniru/Downloads/allocation_output.csv"
        try:
            allocation.to_csv(output_path, index=False)
            print(f"Saved allocation to {output_path}")
        except Exception as e:
            print(f"Error saving allocation: {str(e)}")

        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
