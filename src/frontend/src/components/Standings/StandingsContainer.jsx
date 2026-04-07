import "./StandingsContainer.css";

function StandingsContainer({team}){

    const teamSelected = team;

    return(
        <div className="team-info-div-container">Standings
            {
                teamSelected ? (<p>{teamSelected} current standings</p>):(<p>Overall standings</p>)
            }
        </div>
    )
}

export default StandingsContainer