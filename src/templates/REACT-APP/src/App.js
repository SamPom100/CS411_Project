import logo from './vacation.png';
import './App.css';
import axios from 'axios';
import { useState } from 'react';

function App() {
  const [weather, setWeather] = useState('');

  const callApi = () => {
    axios.get('http://localhost:5000/weather').then((res) => {
      setWeather(res.data);
      console.log(res.data);
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
           <code></code> Welcome to Our Travel Planner.
        </p>
        <a
          className="App-link"
          href="http://localhost:5000/weather" //login page 
          target="_blank"
          rel="noopener noreferrer"
        >
         Login Here
        </a>

        <button
              onClick={callApi}
              className="inline-flex text-white bg-green-500 border-0 py-2 px-6 focus:outline-none hover:bg-green-600 rounded text-lg mr-4 mb-4">
              API CALL BUTTON
        </button>

        <p>
          {weather}
        </p>
      </header>
    </div>
  );
}

export default App;
