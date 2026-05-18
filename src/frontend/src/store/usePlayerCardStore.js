import { create } from "zustand";

const usePlayerCardStore = create((set) => ({
    selectedPlayer: [],
    isOpen: false,

    setPlayer: (player_id) =>
        set({
            selectedPlayer: player_id
        }),

    openPlayerCard: (player_id) =>
        set ({
            selectedPlayer: player_id,
            isOpen: true
        }),

    closePlayerCard: () => ({
        selectedPlayer: null,
        isOpen: false
    })

}));

export default usePlayerCardStore;