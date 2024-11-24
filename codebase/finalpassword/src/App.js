import logo from './logo.svg';
import './App.css';
import { Fragment } from 'react';
import Login from './Login/Login.jsx';

function App() {
  return (
    <Fragment className="App">
      <header className="App-header">
        <Login/>
      </header>
    </Fragment>
  );
}

export default App;
