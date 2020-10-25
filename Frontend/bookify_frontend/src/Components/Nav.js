import React from 'react'
import {Link} from 'react-router-dom'

function Nav() {
    return (
        <nav>
            <h3>Logo</h3>
            <ul className="nav-links"></ul>
                <Link to="/freebook">
                    <li>Freebook</li>
                </Link>
                <Link to="/signup"> 
                <li>SignUp</li>
                </Link>
                
        </nav>
    )
}

export default Nav
