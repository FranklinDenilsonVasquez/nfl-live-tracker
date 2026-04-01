import React from "react";
import "./WeekScroller.css";
import { useWeekStore } from "../store/weekStore"


function WeekScroller() {
    const { selectedWeek, setWeek } = useWeekStore();

    return (
        <div className="week-scroller-container">
            <div className="week_scroller">
                <button  className="arrow-button" onClick={() => setWeek(Math.max(selectedWeek - 1, 1))}>
                    &lt;
                </button>
                    <span> Week {selectedWeek} </span>
                <button  className="arrow-button" onClick={() => setWeek(Math.min(selectedWeek + 1, 18))}>
                    &gt;
                </button>
            </div>

        </div>
    );
}

export default WeekScroller;