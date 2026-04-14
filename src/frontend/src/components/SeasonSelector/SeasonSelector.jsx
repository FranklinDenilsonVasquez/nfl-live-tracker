import React from "react";
import "./SeasonSelector.css";
import { useSeasonStore} from "../../store/seasonStore";
import useGameStore from "../../store/useGameStore";

function SeasonSelector() {

    const { season, setSeason} = useGameStore();

    const seasons = Array.from({ length: 10 }, (_, i) => new Date().getFullYear() - i);
    if (season === undefined) return null;

    return(
        <div className="season-dropdown-container">
            <select
                className="season-dropdown"
                value={ season }
                onChange={(e) => setSeason(Number(e.target.value))}>
                {seasons.map((year) => (
                    <option key={year.toString()} value={year.toString()}>
                        {year} Season
                    </option>
                ))}
            </select>
        </div>
    )
}

export default SeasonSelector;
