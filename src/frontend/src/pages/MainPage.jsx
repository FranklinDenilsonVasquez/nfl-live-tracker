import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer/footer";
import Header from "../components/Header/Header";
import GameList from "../components/GameList/GameList";
import WeekScroller from "../components/WeekScroller/WeekScroller";

export default function HomePage() {
  return (
    <div className="app-container">
      <Header />
      <WeekScroller />
      <GameList/>
      <Footer />
    </div>
  );
}
