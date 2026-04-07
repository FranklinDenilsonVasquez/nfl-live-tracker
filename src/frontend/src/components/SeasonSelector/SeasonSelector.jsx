import React from "react"
import "./SeasonSelector.css"
import { useSeasonStore} from "../../store/seasonStore";

function SeasonSelector() {

    const { seasons, selectedSeason, setSeason } = useSeasonStore();


    return(
        <div className="season-dropdown-container">
            <select
                className="season-dropdown"
                value={ selectedSeason }
                onChange={(e) => setSeason(Number(e.target.value))}>
                {seasons.map((year) => (
                    <option key={year} value={year}>{year}</option>
                ))}
            </select>
        </div>
    )
}

export default SeasonSelector;
