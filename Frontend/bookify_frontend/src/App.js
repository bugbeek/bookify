import './App.css';
import React from 'react';
import {BrowserRouter as Router,Switch, Route} from 'react-router-dom';
import Homepage from './Components/Homepage';
import Freebook from './Components/Freebook';
import Nav from './Components/Nav';
import SignUp from './Components/Signup';

function App() {
  return (
    <Router>
        <div className="App">
          <Nav />
          <Switch>
            <Route path="/" exact component={Homepage}/>
            <Route path = "/freebook" component={Freebook}/>
            <Route path = "/signup" component={SignUp}/>
          </Switch>
        </div>
    </Router>

  );
}

export default App;
