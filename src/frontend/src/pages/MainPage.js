import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer";
import Header from "../components/Header";

export default function HomePage() {
  return (
    <div className="app-container">
      <Header />
      <main className="main-container">
        <div className="team-info-div-container">Teams
          <div className="team-info-group-container">AFC
            <ul>
              <li className="team-info-division-list">Team 1</li>
              <li className="team-info-division-list">Team 2</li>
            </ul>
          </div>
          <div className="team-info-group-container">NFC
            <ul>
              <li className="team-info-division-list">Team 1</li>
              <li className="team-info-division-list">Team 2</li>
            </ul>
          </div>
        </div>
        <div className="schedule-div-container"> Schedlue Info</div>
        <div className="team-info-div-container">Standings</div>
      </main>
      <Footer />
    </div>
  );
}
