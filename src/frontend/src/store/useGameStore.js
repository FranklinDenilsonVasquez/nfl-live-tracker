import { create } from "zustand";
import { apiClient } from "../utils/apiClient";

const currentYear = new Date().getFullYear();

const useGameStore = create((set, get) => ({
  games: [],
  season: currentYear,
  week: "Week 1",
  stage: "Regular Season",
  loading: false,
  showScore: false,
  error: null,
  selectedGameId: null,
  homeTeamId: null,
  awayTeamId: null,
  offensiveSide: "home",

  setSeason: (season) => set({ season, error: null }),
  setWeek: (week) => set({ week }),
  setStage: (stage) => set({ stage }),
  setShowScore: (showScore) => set({ showScore }),
  setGames: (games) => set({ games }),
  toggleOffensiveSide: () =>
    set((state) => ({
      offensiveSide: state.offensiveSide === "home" ? "away" : "home",
    })),

  setSelectedGameId: (gameId) => {
    console.log("Setting Game ID:", gameId);
    set({
      selectedGameId: gameId,
      homeTeamId: gameId.home_team_id,
      awayTeamId: gameId.away_team_id,
    });
  },

  fetchGames: async () => {
    const { season, week, stage } = get();
    // console.log("Fetching games for:", season, `${week}`, `${stage}`);
    set({ loading: true });

    try {
      const response = await apiClient.get(
        `/games/game_list?season=${season}&week=${encodeURIComponent(
          week,
        )}&stage=${encodeURIComponent(stage)}`,
      );

      set({
        games: response.data,
        loading: false,
        error: null,
      });
    } catch (error) {
      set({
        error: error.response?.data?.detail || error.message,
        games: [],
        loading: false,
      });
    }
  },
}));

export default useGameStore;
