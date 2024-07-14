#Tech-Fest Web DEVELOPMENT
# Hospitality Process Digitalization

This project digitalizes the process of allocating rooms in a hostel based on group and hostel data provided in CSV files.

## Features
- Upload group and hostel data files in CSV format.
- Automatically allocate rooms based on the group and hostel data.
- Download the allocation result in a CSV file.

## Project Structure
- `app.py`: The backend Flask application handling file uploads and room allocations.
- `frontend/`: The React frontend application for user interaction.

## Running the Application

### Prerequisites
- Python 3.x
- Node.js
- npm (Node Package Manager)

### Backend Setup
1. Navigate to the project root directory.
2. Install the required Python packages:
   ```bash
   pip install flask pandas flask-cors

3. Run App.py File
   ```bash
   python app.py
###Frontend Setup
1.Navigate to the frontend directory:
   ```bash
    cd frontend
```
2.Install the required npm packages:
   ```bash
     npm install
```
3. Start the React application:
   ```bash
   npm start

###Usage
1.Open your web browser and navigate to http://localhost:3000.
2.Upload your group and hostel CSV files.
3.Click on "Upload and Allocate" to process the files and get the allocation result.
4.Download the resulting allocation CSV file.
Example Files
Include example CSV files in your repository for easy testing:
group.csv
hotel.csv

