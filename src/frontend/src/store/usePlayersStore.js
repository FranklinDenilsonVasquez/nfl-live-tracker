import { create } from "zustand";
import axios from "axios"
import useGameStore from "./useGameStore";

const usePlayersStore = create((set) => ({
    players: [],
    rosters: {
        home: [],
        away: []
    },
    loadingPlayers: false,
    loadingRosters: false,
    error: null,

    setRoster: (type, data) => set((state) => ({
        rosters: {
            ...state.rosters,
            [type]: data
        }
    })),

    fetchGamePlayers: async (game_id) => {
        set({ loadingPlayers: true });

        try {
            const { data } = await axios.get(
                `http://127.0.0.1:8000/games/${game_id}/player-stats`
            );

            console.log("Game Id: ", game_id)
            console.log("API Response: ", data);

            set({
                players: data,
                loadingPlayers: false
            })
        } catch (error) {
            set({
                error: error.message,
                players: [],
                loadingPlayers: false
            })
        }
    },

    fetchGameRoster: async (team_id, season) => {
        try{
            const { data } = await axios.get(
                `http://127.0.0.1:8000/teams/${team_id}/players?season=${season}`
            );

            return data;
        } catch (error) {
            set({
                error: error.message
                });
            return [];
        }
    }
}));
export default usePlayersStore;