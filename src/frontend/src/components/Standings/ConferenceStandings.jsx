import "./StandingsContainer.css";
import DivisionTable from "./DivisionTable";

function ConferenceStandings({ label, divisions }) {
  return (
    <div className="conference-container">
      <div className="conference-header"> {label} </div>
      {Object.entries(divisions).map(([division, standings]) => (
        <DivisionTable
          key={division}
          division={division}
          standings={standings}
        />
      ))}
    </div>
  );
}

export default ConferenceStandings;
