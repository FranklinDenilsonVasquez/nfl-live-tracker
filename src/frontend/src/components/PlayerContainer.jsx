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
            {/* OFFENSE */}
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

            {/* DEFENSE */}
            <button className="player-button DT1">DT1</button>
            <button className="player-button DT2">DT2</button>
            <button className="player-button DE1">DE1</button>
            <button className="player-button DE2">DE2</button>
            <button className="player-button CB1">CB1</button>
            <button className="player-button CB2">CB2</button>
            <button className="player-button CB3">CB3</button>
            <button className="player-button LB1">LB1</button>
            <button className="player-button LB2">LB2</button>
            <button className="player-button FS">FS</button>
            <button className="player-button SS">SS</button>

        </div>
    )
}

export default PlayerContainer