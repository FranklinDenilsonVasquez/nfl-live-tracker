import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer";
import Header from "../components/Header";
import TeamList from "../components/TeamList";


export default function HomePage() {
  return (
    <div className="app-container">
      <Header />
      <TeamList/>
      <Footer />
    </div>
  );
}
