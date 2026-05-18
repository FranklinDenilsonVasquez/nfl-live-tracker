import React from "react";
import "./MainPage.css";
import Footer from "../components/Footer/footer";
import Header from "../components/Header/Header";
import GameList from "../components/GameList/GameList";
import WeekScroller from "../components/WeekScroller/WeekScroller";
import PlayerCard from "../components/PlayerCard/PlayerCard";

export default function HomePage() {
        return (
            <div className="app-container">
                <Header />
                <WeekScroller />
                <GameList/>
                <Footer />
                <PlayerCard/>
            </div>
        );
    }
