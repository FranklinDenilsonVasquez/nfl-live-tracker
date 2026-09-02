import "./StatsSection.css";
import { useEffect, useState } from "react";
import { positionStatsGroup } from "../../utils/positionStatsGroup";

function StatsSection({ player, roster }) {
  // console.log("Player in stat section: ", player)
  // console.log("Roster in stat section: ", roster)
  const statsToShow =
    positionStatsGroup[player.position] || positionStatsGroup.default;

  const groupNames = Object.keys(statsToShow || {});

  const [activeGroup, setActiveGroup] = useState(groupNames[0]);

  // Different positions expose different stat groups, so the previously
  // active tab may not exist for a newly selected player.
  useEffect(() => {
    setActiveGroup(groupNames[0]);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [player?.player_id, player?.position]);

  // Fallback if no group exists
  if (!statsToShow || groupNames.length === 0) {
    return (
      <div className="player-stats-section">
        <div className="no-data-found">No Data Found</div>
      </div>
    );
  }

  const currentGroup = statsToShow[activeGroup] ? activeGroup : groupNames[0];
  const stats = statsToShow[currentGroup] || [];

  return (
    <div className="player-stats-section">
      <div className="stat-group-tabs">
        {groupNames.map((groupName) => (
          <button
            key={groupName}
            type="button"
            className={
              "stat-group-tab" + (groupName === currentGroup ? " active" : "")
            }
            onClick={() => setActiveGroup(groupName)}
          >
            {groupName.toUpperCase()}
          </button>
        ))}
      </div>

      <div className="stat-group">
        {stats.map(({ key, label }) => {
          const value = player?.stats?.[currentGroup]?.[key];

          return (
            <div key={key} className="stat-row">
              <span className="stat-label">{label} </span>
              <span className="stat-value">{value ? value : "0"}</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}

export default StatsSection;
