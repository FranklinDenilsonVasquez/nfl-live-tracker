import { create } from "zustand";

const useUiStore = create((set) => ({
  activePanel: null, // null | "games" | "standings"

  togglePanel: (panel) =>
    set((state) => ({
      activePanel: state.activePanel === panel ? null : panel,
    })),

  closePanel: () => set({ activePanel: null }),
}));

export default useUiStore;
