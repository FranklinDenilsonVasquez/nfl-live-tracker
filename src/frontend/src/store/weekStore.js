import { create } from "zustand";

/*
    Zustand is a small tool that holds data that we want to share between
    components. This avoids passing props down through multiple layers and
    keeps shared state easy to manage
*/

// useWeekStore stores the selected week & season while also holding two set functions
export const useWeekStore = create((set) => ({
    selectedWeek: 1,
    setWeek: (week) => set({ selectedWeek: week}),
}));