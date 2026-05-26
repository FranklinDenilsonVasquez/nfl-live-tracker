import { create } from "zustand";
import "./PlayerCard.css";
import usePlayerStore from "../../store/usePlayersStore";
import usePlayerCardStore from "../../store/usePlayerCardStore";
import { useEffect, useMemo } from "react";
import usePlayersStore from "../../store/usePlayersStore";
import useGameStore from "../../store/useGameStore";
import { MdHighlightOff, MdAccountCircle } from "react-icons/md";
import { findPlayerTeam } from "../../utils/findPlayerTeam";
import { useSeasonStore } from "../../store/seasonStore";
import StatsSection from "./StatsSection";

function PlayerCard() {
  const players = usePlayersStore((state) => state.players);
  const { selectedSeason } = useSeasonStore();
  const { rosters } = usePlayerStore();
  const { selectedPlayer, isOpen, openPlayerCard, closePlayerCard } =
    usePlayerCardStore();
  const { selectedGameId, homeTeamId, awayTeamId } = useGameStore();

  const selectedGame = useGameStore((state) =>
    state.games.find((g) => g.game_id === state.selectedGameId),
  );
  console.log(selectedGame);

  const allPlayers = useMemo(
    () => ({
      home_team: players?.home_team || [],
      away_team: players?.away_team || [],
    }),
    [players],
  );

  const player = useMemo(() => {
    const flatRoster = Object.values(rosters || {}).flat();
    const flatStats = Object.values(allPlayers || {}).flat();
    const teamAffiliation = findPlayerTeam(rosters, selectedPlayer);
    const foundPlayer =
      flatStats.find((player) => player.player_id === selectedPlayer) ||
      flatRoster.find((player) => player.player_id === selectedPlayer);

    return {
      ...foundPlayer,
      team: teamAffiliation,
    };
  }, [rosters, allPlayers, selectedPlayer]);

  console.log("players: ", player);
  //   console.log(
  //     "Rosters: ",
  //     rosters?.home?.find((p) => p.player_id === selectedPlayer)?.jersey_number,
  //   );

  useEffect(() => {
    closePlayerCard();
  }, [selectedGameId, selectedSeason]);

  return (
    <>
      {isOpen && (
        <div>
          <div className="player-card-container" style={{ color: "white" }}>
            <div className="player-card">
              <div className="player-image-section">
                <div className="image-container">
                  {player?.player_img ? (
                    <img
                      src={player?.player_img}
                      alt={player?.player_name}
                    ></img>
                  ) : (
                    <MdAccountCircle
                      style={{
                        inset: 0,
                        height: "100%",
                        width: "100%",
                        opacity: 0.25,
                      }}
                    />
                  )}
                </div>
                <div className="bio-section">
                  <div className="name-section">
                    {player ? player.player_name : "Unknown"}
                  </div>
                  <div className="position-section">
                    {player ? player.position : "N/A"}
                    <div className="bio-shadow-text"> Position </div>
                  </div>
                  <div className="team-section">
                    {player && player?.team?.team === "home" ? (
                      <img
                        src={selectedGame?.home_team?.logo}
                        alt={selectedGame?.home_team?.team_name}
                      ></img>
                    ) : (
                      <img
                        src={selectedGame?.away_team?.logo}
                        alt={selectedGame?.away_team?.team_name}
                      ></img>
                    )}
                    <div className="bio-shadow-text"> Team </div>
                  </div>
                  <div className="jersey-num-section">
                    #{" "}
                    {player && player?.team?.team === "home"
                      ? rosters?.home?.find(
                          (p) => p.player_id === selectedPlayer,
                        )?.jersey_number
                      : rosters?.away?.find(
                          (p) => p.player_id === selectedPlayer,
                        )?.jersey_number}
                    <div className="bio-shadow-text"> Number </div>
                  </div>
                </div>
              </div>
              <StatsSection player={player} roster={rosters} />
            </div>
            <button className="close-player-card-btn" onClick={closePlayerCard}>
              <MdHighlightOff />
            </button>
          </div>
        </div>
      )}{" "}
    </>
  );
}

export default PlayerCard;
