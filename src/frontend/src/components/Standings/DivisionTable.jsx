import { useMemo } from "react";
import "./StandingsContainer.css";
import { calculateWinPct } from "../../utils/calculateWinPct";

function DivisionTable({ division, standings }) {
  return (
    <div className="division-container">
      <div className="table-wrapper">
        <div className="row-header">
          <div className="legend-stat">{division}</div>
          <div className="legend-stat">W</div>
          <div className="legend-stat">D</div>
          <div className="legend-stat">L</div>
          <div className="legend-stat">PCT</div>
          <div className="legend-stat">PF</div>
          <div className="legend-stat">PA</div>
          <div className="legend-stat">DIFF</div>
          <div className="legend-stat">DW</div>
          <div className="legend-stat">DL</div>
          <div className="legend-stat">CW</div>
          <div className="legend-stat">CL</div>
          <div className="legend-stat">HW</div>
          <div className="legend-stat">HL</div>
          <div className="legend-stat">RW</div>
          <div className="legend-stat">RL</div>
          <div className="legend-stat">STRK</div>
        </div>

        {standings.map((team) => (
          <div className="row" key={team.team.team_id}>
            <div className="team-display">
              <img
                className="standing-team-logo"
                src={team?.team?.logo}
                alt={team.team.team_name}
              ></img>
            </div>
            <div className="stat">{team.wins}</div>
            <div className="stat">{team.ties}</div>
            <div className="stat">{team.losses}</div>
            <div className="stat">
              {calculateWinPct(team.wins, team.losses, team.ties)}
            </div>
            <div className="stat">{team.points_for}</div>
            <div className="stat">{team.points_against}</div>
            <div className="stat">{team.point_differential}</div>
            <div className="stat">{team.division_wins}</div>
            <div className="stat">{team.division_losses}</div>
            <div className="stat">{team.conference_wins}</div>
            <div className="stat">{team.conference_losses}</div>
            <div className="stat">{team.home_wins}</div>
            <div className="stat">{team.home_losses}</div>
            <div className="stat">{team.road_wins}</div>
            <div className="stat">{team.road_losses}</div>
            <div className="stat">{team.streak}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DivisionTable;
