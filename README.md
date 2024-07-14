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
