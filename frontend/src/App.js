
// import React from 'react';
// import './App.css';
// import FileUpload from './FileUpload';

// function App() {
//     return (
//         <div className="App">
//             <header className="App-header">
//                 <h1>Hospitality Process Digitalization</h1>
//             </header>
//             <FileUpload />
//         </div>
//     );
// }

// export default App;
import React from 'react';
import './App.css';
import FileUpload from './FileUpload';
import logo from './tech.png';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <h1>Hospitality Process Digitalization</h1>
            </header>
            <main className="App-main">
                <FileUpload />
            </main>
            <footer className="App-footer">
                <p>&copy; Techfest 2024</p>
            </footer>
        </div>
    );
}

export default App;
