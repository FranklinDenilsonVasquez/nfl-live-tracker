import { create } from "zustand";
import "./PlayerCard.css";
import usePlayerStore from "../../store/usePlayersStore";
import usePlayerCardStore from "../../store/usePlayerCardStore";
import {useEffect, useMemo} from "react";
import usePlayersStore from "../../store/usePlayersStore";
import useGameStore from "../../store/useGameStore";

function PlayerCard() {
    const players = usePlayersStore((state) => state.players);
    const { rosters } = usePlayerStore();
    const { selectedPlayer, isOpen, openPlayerCard, closePlayerCard } = usePlayerCardStore();
    const { selectedGameId, homeTeamId, awayTeamId } = useGameStore();
    const homeTeam = useGameStore(
        (state) => state.homeTeamId
    );

    const allPlayers = {
        "home_team": players?.home_team || [],
        "away_team": players?.away_team || []
    };

    const player = useMemo(() => {
        const flatRoster = Object.values(rosters || {}).flat();
        const flatStats = Object.values(allPlayers || {}).flat();

        return (
            flatStats.find(player => player.player_id === selectedPlayer) ||
            flatRoster.find(player => player.player_id === selectedPlayer)
        );
    }, [rosters, allPlayers, selectedPlayer]);
    console.log(player)

    return (
        <div>
            hi
        </div>
    )

}


export default PlayerCard;
