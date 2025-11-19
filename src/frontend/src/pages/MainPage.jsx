import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer";
import Header from "../components/Header";
import TeamList from "../components/TeamList";
import DateScroller from "../components/DateScroller";

export default function HomePage() {
  return (
    <div className="app-container">
      <Header />
      <DateScroller />
      <TeamList/>
      <Footer />
    </div>
  );
}
