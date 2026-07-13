import { create } from "zustand";
import { apiClient } from "../utils/apiClient";

const useStandingStore = create((set, get) => ({
  data: [],
  loadingStandings: false,
  error: false,

  fetchStandings: async (season_year) => {
    set({
      loadingStandings: true,
      error: null,
    });

    try {
      const { data } = await apiClient.get(
        `/standing/${season_year}`,
      );
      // console.log("Standings data: ", data);

      set({
        data: data.standings,
        loadingStandings: false,
      });
    } catch (error) {
      set({
        error: error.message ?? "Failed to load standings",
        data: [],
        loadingStandings: false,
      });
    }
  },
}));
export default useStandingStore;
