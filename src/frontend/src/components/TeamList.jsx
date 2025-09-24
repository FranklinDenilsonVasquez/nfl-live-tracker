import React, { useState } from "react";
import "./TeamList.css";

function TeamList(){

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
                <div className="schedule-div-container"> 
                    {teamSelected ? (<p>Selected team {teamSelected}</p>):(<p>Select a team for their schedule</p>)}
                </div>
                <div className="team-info-div-container">Standings
                    {
                        teamSelected ? (<p>{teamSelected} current standings</p>):(<p>Overall standings</p>)
                    }
                </div>
            </main>
        </div>
    )
}

export default TeamList