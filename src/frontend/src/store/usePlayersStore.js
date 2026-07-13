import { create } from "zustand";
import { apiClient } from "../utils/apiClient";
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
            const { data } = await apiClient.get(
                `/games/${game_id}/player-stats`
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
            const { data } = await apiClient.get(
                `/teams/${team_id}/players?season=${season}`
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