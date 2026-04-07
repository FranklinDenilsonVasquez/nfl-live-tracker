import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer/footer";
import Header from "../components/Header/Header";
import TeamList from "../components/TeamList/TeamList";
import WeekScroller from "../components/WeekScroller/WeekScroller";

export default function HomePage() {
  return (
    <div className="app-container">
      <Header />
      <WeekScroller />
      <TeamList/>
      <Footer />
    </div>
  );
}
