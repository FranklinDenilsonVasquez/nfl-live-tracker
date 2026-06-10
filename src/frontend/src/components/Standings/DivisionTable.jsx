import "./StandingsContainer.css";

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
            <div className="stat">{team.wins}</div>
            <div className="stat">{team.points_for}</div>
            <div className="stat">{team.points_against}</div>
            <div className="stat">{team.point_differential}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default DivisionTable;
