import React, {useEffect} from "react";
import "./WeekScroller.css";
import { useWeekStore } from "../../store/weekStore"
import SeasonSelector from "../SeasonSelector/SeasonSelector";
import useGameStore from "../../store/useGameStore";


function WeekScroller() {
    const { weekIndex, nextWeek, prevWeek, weeks } = useWeekStore();
    const { setWeek, setStage } = useGameStore();
    const currentWeek = weeks[weekIndex];

    useEffect(() => {
        setWeek(currentWeek.label);
        setStage(currentWeek.stage);
    }, [weekIndex, currentWeek, setWeek, setStage]);

    return (
        <div className="week-scroller-container">
            <div className="week_scroller">
                <button  className="arrow-button" onClick={prevWeek}>
                    &lt;
                </button>
                    <span style={{ fontSize: "15px" }}> {currentWeek.label}</span>
                <button  className="arrow-button" onClick={nextWeek}>
                    &gt;
                </button>
                <SeasonSelector/>
            </div>
        </div>
    );
}

export default WeekScroller;