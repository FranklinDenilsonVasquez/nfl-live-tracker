import React, { useState, useEffect } from "react";
import "./GameList.css";
import { useSeasonStore } from "../../store/seasonStore";
import FieldContainer from "../Field/FieldContainer";
import StandingsContainer from "../Standings/StandingsContainer";
import useGameStore from "../../store/useGameStore";
import useUiStore from "../../store/useUiStore";
import { MdVisibility, MdVisibilityOff } from "react-icons/md";

function GameList() {
  const [selectedGame, setGameSelected] = useState(null);

  const {
    games,
    week,
    season,
    loading,
    error,
    setSeason,
    setWeek,
    fetchGames,
    showScore,
    setShowScore,
    selectedGameId,
    setSelectedGameId,
  } = useGameStore();

  const { selectedSeason } = useSeasonStore();
  const { activePanel, togglePanel, closePanel } = useUiStore();

  useEffect(() => {
    setShowScore(false);
  }, []);

  // Close open drawer on Escape and lock body scroll while it is open
  useEffect(() => {
    if (!activePanel) return;
    const onKeyDown = (e) => {
      if (e.key === "Escape") closePanel();
    };
    window.addEventListener("keydown", onKeyDown);
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKeyDown);
      document.body.style.overflow = "";
    };
  }, [activePanel, closePanel]);

  useEffect(() => {
    if (selectedSeason !== undefined) {
      setSeason(selectedSeason);
    }
  }, [selectedSeason, setSeason]);

  useEffect(() => {
    if (season !== undefined && week !== undefined) {
      fetchGames();
    }
  }, [season, week, fetchGames]);

  const onClickGameIdSelect = (gameId) => {
    console.log("Selected game: ", gameId);
    setSelectedGameId(gameId);
  };

  const onClickTeamSelect = (game) => {
    console.log("Selected game: ", game);
    setGameSelected(game);
  };

  const handleGameClick = (game) => {
    onClickTeamSelect(game);
    onClickGameIdSelect(game.game_id);
    closePanel();
  };

  // console.log("Games array:", games);
  return (
    <div>
      <main className="main-container">
        <button
          className="drawer-toggle drawer-toggle-left"
          onClick={() => togglePanel("games")}
          aria-expanded={activePanel === "games"}
        >
          Games
        </button>
        <button
          className="drawer-toggle drawer-toggle-right"
          onClick={() => togglePanel("standings")}
          aria-expanded={activePanel === "standings"}
        >
          Standings
        </button>
        {activePanel && (
          <div className="drawer-backdrop" onClick={closePanel} />
        )}
        <div
          className={`team-info-div-container games-panel ${
            activePanel === "games" ? "open" : ""
          }`}
        >
          <p className="game-list-header">
            Games
            <button
              onClick={() => setShowScore(!showScore)}
              className="eye-button"
              title="Toggel scores"
            >
              {showScore ? <MdVisibility /> : <MdVisibilityOff />}
            </button>
          </p>
          {loading && <p className="loading-wheel"></p>}
          {error && <p className="error-text"> {error} </p>}
          {!loading && !error && (
            <ul>
              {games.map((game, idx) => (
                <li
                  key={idx}
                  className="team-info-division-list"
                  style={
                    selectedGame === game
                      ? {
                          backgroundColor: "#0c5623",
                        }
                      : {}
                  }
                  onClick={() => handleGameClick(game)}
                >
                  <img
                    src={game.home_team.logo}
                    alt={game.home_team.team_name}
                    className="team_logo"
                  />

                  {showScore ? (
                    <>
                      {game.home_team_score} - {game.away_team_score}
                    </>
                  ) : (
                    <span style={{ color: "white" }}>vs. </span>
                  )}
                  <img
                    src={game.away_team.logo}
                    alt={game.away_team.team_name}
                    className="team_logo"
                  />
                </li>
              ))}
            </ul>
          )}
          {!loading && !error && games.length === 0 && <p>No games found.</p>}
        </div>
        <div className="resizable-div-container">
          <FieldContainer game={selectedGame} />
        </div>
        <StandingsContainer game={selectedGame} />
      </main>
    </div>
  );
}

export default GameList;
