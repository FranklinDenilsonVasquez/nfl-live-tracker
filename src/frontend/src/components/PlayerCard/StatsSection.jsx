import "./StatsSection.css";
import { positionStatsGroup } from "../../utils/positionStatsGroup";

function StatsSection({ player, roster }) {
  // console.log("Player in stat section: ", player)
  // console.log("Roster in stat section: ", roster)
  const statsToShow =
    positionStatsGroup[player.position] || positionStatsGroup.default;

  // Fallback if no group exists
  if (!statsToShow || Object.keys(statsToShow).length === 0) {
    return (
      <div className="player-stats-section">
        <div className="no-data-found">No Data Found</div>
      </div>
    );
  }

  return (
    <div className="player-stats-section">
      {Object.entries(statsToShow).map(([groupName, stats]) => (
        <div key={groupName} className="stat-group">
          <div className="group-name">{groupName.toUpperCase()}</div>

          {stats.map(({ key, label }) => {
            const value = player?.stats?.[groupName]?.[key];

            if (value == null) {
              return (
                <div key={key} className="stat-row">
                  <span className="stat-label">{label} </span>
                  <span className="stat-value">{value ? value : "0"}</span>
                </div>
              );
            }

            return (
              <div key={key} className="stat-row">
                <span className="stat-label">{label} </span>
                <span className="stat-value">{value}</span>
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}

export default StatsSection;
