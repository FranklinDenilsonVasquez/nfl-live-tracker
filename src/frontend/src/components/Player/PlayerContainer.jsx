import React, {useEffect, useMemo, useState} from "react";
import "./PlayerContainer.css";
import usePlayerStore from "../../store/usePlayersStore";
import useGameStore from "../../store/useGameStore";
import { groupPlayersByPosition } from "../../utils/groupPlayersByPosition";
import { calculateImpactScore } from "../../utils/calculateImpactScore";
import { lineup } from "../../utils/lineupConfig";
import { getIndexFromSlot } from "../../utils/getIndexFromSlot";
import {useSeasonStore} from "../../store/seasonStore";
import { MdAccountCircle } from "react-icons/md";
import usePlayerCardStore from "../../store/usePlayerCardStore";

function PlayerContainer({game, players}) {
    const { fetchGameRoster, fetchGamePlayers, setRoster, rosters } = usePlayerStore();
    const { selectedSeason } = useSeasonStore();
    const { setPlayer, openPlayerCard } = usePlayerCardStore();

    const homePlayers = players?.home_team || [];
    const awayPlayers = players?.away_team || [];
    // console.log("HHHHHHH", homePlayers)
    // console.log("PPPPP", awayPlayers)

    useEffect(() => {
        if (!game?.home_team?.team_id || !game?.away_team?.team_id || !selectedSeason) return;

        const loadRosters = async () => {

           setRoster("home", [])
           setRoster("away", [])


            const home = await fetchGameRoster(game.home_team.team_id, selectedSeason);
            const away = await fetchGameRoster(game.away_team.team_id, selectedSeason);

            setRoster("home", home)
            setRoster("away", away)
            // console.log("HomeRoster: ", home)
        };

        loadRosters();
    }, [game?.home_team?.team_id, game?.away_team?.team_id, selectedSeason]);

    const mergeRosterWithStats = (roster, statsPlayers) => {
        const statsMap = new Map(
            statsPlayers.map(p => [Number(p.player_id), p])
        );

        // console.log("Stats Map: ", statsMap)

            return roster.map(player => {
                const stats = statsMap.get(Number(player.player_id));

                // console.log("Player_id: ", player.player_id, player.player_name)
                // console.log("Stats for player " + player.player_id , player.player_name + " :", stats?.stats ?? null)

                return {
                    ...player,
                    stats: stats?.stats ?? null,
                };
            });
    }

    const groupedPlayers = useMemo(() => {
        const homeRoster = rosters.home
        const awayRoster = rosters.away
        const homeMerged = mergeRosterWithStats(homeRoster, homePlayers);
        // console.log("Home roster before merge: ", homeRoster)
        // console.log("HomeMerged: ", homeMerged)

        const awayMerged = mergeRosterWithStats(awayRoster, awayPlayers);
        // console.log("Away roster before merge: ", awayRoster)
        // console.log("AwayMerged: ", awayMerged)

        const groupAndRank = (rosters, players) => {
            const grouped = groupPlayersByPosition(players);
            // console.log("Grouped: ", grouped)

            const result = {};

            for (const position in grouped) {
                result[position] = grouped[position].map(player => ({
                    ...player,
                    impactScore: calculateImpactScore(player)
                })).sort((a , b) => b.impactScore - a.impactScore)
            }

            return result;
        };

        return {
            groupedHomePlayers: groupAndRank(homeRoster, homeMerged),
            groupedAwayPlayers: groupAndRank(awayRoster, awayMerged)
        };

    }, [homePlayers, awayPlayers, rosters]);


    // Debug for loop to count the players in groupedHomePlayers for correctness
    // let count = 0;
    //     for (const [position, players] of Object.entries(groupedPlayers.groupedHomePlayers)) {
    //         count += players.length;
    //     }
    //     console.log("length: ", count)

    // Debugging
    // console.log("This is the player list for home players: ", groupedPlayers.groupedHomePlayers)
    // console.log("This is the player list for away players: ", groupedPlayers.groupedAwayPlayers)

    // console.log("Impact array for home players: ", playerImpactCalculation.homePlayerImpactRanking)
    // console.log("Impact array for away players: ", playerImpactCalculation.awayPlayerImpactRanking)

    const handleClick = (player) => {
        if (!player) return;

        setPlayer(player?.player_id);
        openPlayerCard(player?.player_id);
    }

    return(
        <div>
            {lineup.offense.map(slot => {
                const index = getIndexFromSlot(slot.id);
                const player = groupedPlayers.groupedHomePlayers[slot.position]?.[index];

                return (
                    <button
                        key={slot.id}
                        className={`player-button ${slot.id}`}
                        style={{
                            backgroundImage: player?.player_img
                                ? `url(${player.player_img})`
                                : "none",
                            backgroundSize: "cover",
                            backgroundPosition: "center"
                        }}
                        onClick={() => handleClick(player)}
                    >
                        {(!player || !game) && (
                            <MdAccountCircle style={{
                                position: "absolute",
                                inset: 0,
                                width: "100%",
                                height: "100%",
                                opacity: 0.25,
                                }}
                            />
                        )}
                        <span className="hover-text"> {player ? player.player_name : slot.id} </span>
                    </button>
                );
            })}
            {lineup.defense.map(slot => {
                const index = getIndexFromSlot(slot.id);
                const player = groupedPlayers.groupedAwayPlayers[slot.position]?.[index];
                return(
                    <button
                    key={slot.id}
                    className={`player-button ${slot.id}`}
                    style={{
                        backgroundImage: player?.player_img
                            ? `url(${player.player_img})`
                            : "none",
                        backgroundSize: "cover",
                        backgroundPosition: "center"
                    }}
                    onClick={() => handleClick(player)}
                    >
                        {(!player || !game) && (
                            <MdAccountCircle style={{
                                position: "absolute",
                                inset: 0,
                                width: "100%",
                                height: "100%",
                                opacity: 0.25,
                                }}
                            />
                        )}
                        <span className="hover-text"> {player ? player.player_name : slot.id} </span>
                    </button>
                )
            })}
        </div>
    )
}

export default PlayerContainer