import React, { useState } from "react";
import "./PlayerContainer.css";

function PlayerContainer({team}) {

    const teamSelected = team;

    return(
        <div>
            <button className="playerButton">QB</button>
        </div>
    )
}

export default PlayerContainer