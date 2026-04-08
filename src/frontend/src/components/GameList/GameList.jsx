import React, { useState } from "react";
import "./GameList.css";
import FieldContainer from "../Field/FieldContainer";
import StandingsContainer from "../Standings/StandingsContainer";

function GameList(){

    const [teamSelected, setTeamSelected] = useState("");

    const onClickTeamSelect = (team) => {
        setTeamSelected(team.target.innerText)
    }

    return (
        <div>
            <main className="main-container">
                <div className="team-info-div-container">
                <div className="team-info-group-container">AFC
                    <ul>
                    <li className="team-info-division-list" onClick={onClickTeamSelect}>Team 1</li>
                    <li className="team-info-division-list" onClick={onClickTeamSelect}>Team 2</li>
                    </ul>
                </div>
                <div className="team-info-group-container">NFC
                    <ul>
                    <li className="team-info-division-list" onClick={onClickTeamSelect}>Team 1</li>
                    <li className="team-info-division-list" onClick={onClickTeamSelect}>Team 2</li>
                    </ul>
                </div>
                </div>
                <div className="resizable-div-container"> 
                    <FieldContainer team={teamSelected}/>
                </div>
                <StandingsContainer team={teamSelected} />
            </main>
        </div>
    )
}

export default GameList