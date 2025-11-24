import React, { useState } from "react";
import "./PlayerContainer.css";
import cjStroud from "../img/cj_stroud.jpg";
import PlayerButton from "./PlayerButton";

function PlayerContainer({team}) {

    const teamSelected = team;

    return(
        <div>
            {/*<PlayerContainer className="QB"/>*/}
            {/*<PlayerContainer className="RB"/>*/}
            <button className="player-button WR1">WR1</button>
            <button className="player-button WR2">WR2</button>
            <button className="player-button OL-LT">LT</button>
            <button className="player-button OL-LG">LG</button>
            <button className="player-button OL-C">OL</button>
            <button className="player-button OL-RG">RG</button>
            <button className="player-button OL-RT">RT</button>
            <button className="player-button TE">TE</button>
            <button className="player-button WR3">WR3</button>
            <button className="player-button QB" style={{
                backgroundImage: `url(${cjStroud})`,
                backgroundSize: "cover",
                backgroundPosition: "center"
            }}/>
            <button className="player-button RB">RB</button>
        </div>
    )
}

export default PlayerContainer