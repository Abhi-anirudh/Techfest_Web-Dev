import React, { useState } from 'react';
import axios from 'axios';
import './FileUpload.css';

function FileUpload() {
    const [groupFile, setGroupFile] = useState(null);
    const [hostelFile, setHostelFile] = useState(null);
    const [downloadLink, setDownloadLink] = useState(null);

    const handleGroupFileChange = (e) => setGroupFile(e.target.files[0]);
    const handleHostelFileChange = (e) => setHostelFile(e.target.files[0]);

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('group_file', groupFile);
        formData.append('hostel_file', hostelFile);

        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: { 'Content-Type': 'multipart/form-data' }
            });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            setDownloadLink(url);
        } catch (error) {
            console.error("There was an error uploading the files!", error);
        }
    };

    return (
        <div className="file-upload-box">
            <h2>Upload CSV Files</h2>
            <div className="file-input-section">
                <p>Please upload your group file:</p>
                <input type="file" onChange={handleGroupFileChange} />
            </div>
            <div className="file-input-section">
                <p>Please upload your hostel file:</p>
                <input type="file" onChange={handleHostelFileChange} />
            </div>
            <button onClick={handleUpload}>Upload and Allocate</button>
            {downloadLink && <a href={downloadLink} download="allocation_output.csv">Download Allocation</a>}
        </div>
    );
}

export default FileUpload;
