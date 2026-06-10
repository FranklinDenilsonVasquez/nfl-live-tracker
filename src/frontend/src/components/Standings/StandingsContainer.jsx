import { useEffect, useMemo } from "react";
import useStandingStore from "../../store/useStandingStore";
import { useSeasonStore } from "../../store/seasonStore";
import "./StandingsContainer.css";
import { groupStandings } from "../../utils/groupStandings";
import useGameStore from "../../store/useGameStore";
import ConferenceStandings from "./ConferenceStandings";

function StandingsContainer({ team }) {
  const teamSelected = team;
  const { data, fetchStandings } = useStandingStore();
  const { selectedSeason } = useSeasonStore();
  const { homeTeamId, awayTeamId } = useGameStore();

  useEffect(() => {
    if (selectedSeason !== undefined) {
      const standings = fetchStandings(selectedSeason);
    }
  }, [selectedSeason, fetchStandings]);

  // console.log("Data: ", data);

  const grouped = useMemo(() => {
    return groupStandings(data);
  }, [data]);

  console.log("Grouped Standings: ", grouped);
  // console.log("Home team: ", homeTeamId);
  // console.log("Away team: ", awayTeamId);
  const afc = grouped["American Football Conference"] || {};
  const nfc = grouped["National Football Conference"] || {};

  return (
    <div className="team-info-div-container">
      <p className="standing-list-header">Standings</p>
      <ConferenceStandings label="AFC" divisions={afc} />
      <ConferenceStandings label="NFC" divisions={nfc} />
    </div>
  );
}

export default StandingsContainer;
