import "./FieldContainer.css";
import PlayerContainer from "../Player/PlayerContainer";
import Field from "./Field";
import { useEffect } from "react";
import useGameStore from "../../store/useGameStore";
import usePlayerStore from "../../store/usePlayersStore";
import seasonSelector from "../SeasonSelector/SeasonSelector";
import { useSeasonStore } from "../../store/seasonStore";
import { CgToggleSquareOff, CgToggleSquare } from "react-icons/cg";

function FieldContainer({ game }) {
  const homeLogo = game?.home_team?.logo;
  const awayLogo = game?.away_team?.logo;

  const { selectedGameId, offensiveSide, toggleOffensiveSide } = useGameStore();
  const { fetchGamePlayers, fetchGameRoster, players } = usePlayerStore();
  const { selectedSeason } = useSeasonStore();

  useEffect(() => {
    if (selectedGameId) {
      fetchGamePlayers(selectedGameId);
    }
  }, [selectedGameId]);

  //Debugging
  // console.log("Home team QB: ", players?.home_team?.filter(p => p.position === "QB"))
  // console.log("Away QB: ", players?.away_team?.filter(p => p.position === "QB"));
  //
  // console.log("Home team RB: ", players?.home_team?.filter(p => p.position === "RB"))
  // console.log("Away RB: ", players?.away_team?.filter(p => p.position === "RB"));

  const offenseTeam =
    offensiveSide === "home" ? game?.home_team : game?.away_team;

  return (
    <div className="field-container">
      {game && (
        <button
          className="side-toggle-btn"
          onClick={toggleOffensiveSide}
          title="Swap offensive and defensive sides"
        >
          {offensiveSide === "home" ? (
            <CgToggleSquareOff className="toggle-icon" />
          ) : (
            <CgToggleSquare className="toggle-icon" />
          )}
        </button>
      )}

      <div className="top-endzone">
        {awayLogo ? (
          <div className="endzone-content">
            <img
              src={offensiveSide === "home" ? awayLogo : homeLogo}
              className="endzone-logo"
              alt={game?.away_team?.team_name}
            />
            <p className="endzone-name">
              {offensiveSide === "home"
                ? game.away_team.team_name
                : game.home_team.team_name}
            </p>
            <img
              src={offensiveSide === "home" ? awayLogo : homeLogo}
              className="endzone-logo"
              alt={game?.away_team?.team_name}
            />
          </div>
        ) : (
          <p>NFL</p>
        )}
      </div>
      <div className="field-container-padding"></div>
      <Field />
      <div>
        <div className="field-container-padding">
          <PlayerContainer players={players} game={game} />
        </div>
        <div className="bottom-endzone">
          {homeLogo ? (
            <div className="endzone-content">
              <img
                src={offensiveSide === "home" ? homeLogo : awayLogo}
                className="endzone-logo"
                alt={game?.home_team?.team_name}
              />
              <p className="endzone-name">
                {offensiveSide === "home"
                  ? game.home_team.team_name
                  : game.away_team.team_name}
              </p>
              <img
                src={offensiveSide === "home" ? homeLogo : awayLogo}
                className="endzone-logo"
                alt={game?.home_team?.team_name}
              />
            </div>
          ) : (
            <p>NFL</p>
          )}
        </div>
      </div>
    </div>
  );
}

export default FieldContainer;
