import React, { useState, useEffect } from "react";
import "./GameList.css";
import {useSeasonStore} from "../../store/seasonStore";
import FieldContainer from "../Field/FieldContainer";
import StandingsContainer from "../Standings/StandingsContainer";
import useGameStore from "../../store/useGameStore";
import { MdVisibility, MdVisibilityOff } from "react-icons/md";

function GameList(){

    const [selectedGame, setGameSelected] = useState(null);

    const { games, week, season, loading, error, setSeason, setWeek, fetchGames, showScore, setShowScore} =
        useGameStore();

    const { selectedSeason } = useSeasonStore();

    useEffect(() => {
        setShowScore(false)
    }, []);

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


    const onClickTeamSelect = (game) => {
        setGameSelected(game);
    };
    console.log("Games array:", games);
    return (
        <div>
            <main className="main-container">
               <div className="team-info-div-container">
                    <p className="game-list-header">
                        Games
                        <button
                           onClick={() => setShowScore(!showScore)}
                           className="eye-button"
                            title="Toggel scores">
                           {showScore ? <MdVisibility/> : <MdVisibilityOff/>}
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
                                onClick={() => onClickTeamSelect(game)}>
                                   <img
                                       src={game.home_team.logo}
                                       alt={game.home_team.team_name}
                                       className="team_logo"
                                   />
                                   {showScore ? <>{game.home_team_score} - {game.away_team_score}</> : <>vs.</> }
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
                    <FieldContainer game={selectedGame}/>
                </div>
                <StandingsContainer game={selectedGame} />
            </main>
        </div>
    );
}

export default GameList;