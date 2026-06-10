import axios from "axios";
import { create } from "zustand";

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
      const { data } = await axios.get(
        `http://127.0.0.1:8000/standing/${season_year}`,
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
