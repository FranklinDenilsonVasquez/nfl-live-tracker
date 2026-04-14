import axios from "axios"
import { create } from "zustand"

const currentYear = new Date().getFullYear();

const useGameStore = create((set, get) => ({
    games: [],
    season: currentYear,
    week: "Week 1",
    stage: "Regular Season",
    loading: false,
    showScore: false,
    error: null,

    setSeason: (season) => set({ season, week: "Week 1", stage: "Regular Season", error: null }),
    setWeek: (week) => set({ week }),
    setStage: (stage) => set({ stage }),
    setShowScore: (showScore) => set({ showScore }),

    fetchGames: async () => {
        const { season, week , stage } = get();
        console.log("Fetching games for:", season, `${week}`, `${stage}`);
        set({loading: true});

        try {
            const response = await axios.get(
                `http://127.0.0.1:8000/games/game_list?season=${season}&week=${encodeURIComponent(week)}&stage=${encodeURIComponent(stage)}`
            );

            set({
                games: response.data,
                loading: false,
                error: null
            });
        } catch (error) {
            set({
                error: error.response?.data?.detail || error.message,
                games: [],
                loading: false
            });
        }
    }
}));

export default useGameStore;

