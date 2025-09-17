import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer";
import DateScroller from "../components/DateScroller";

function Header() {
  return (
    <div className="background">
      <div className="header">
        <h1>NFL Stat Tracker</h1>
        <div className="right-buttons">
          <button>Menu</button>
          <button>Search</button>
        </div>
      </div>

      <DateScroller />
    </div>
  );
}

export default Header() 
