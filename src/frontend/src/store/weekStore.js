import { create } from "zustand";

/*
    Zustand is a small tool that holds data that we want to share between
    components. This avoids passing props down through multiple layers and
    keeps shared state easy to manage
*/

const weeks = [
    { label: "Week 1", stage: "Regular Season" },
    { label: "Week 2", stage: "Regular Season" },
    { label: "Week 3", stage: "Regular Season" },
    { label: "Week 4", stage: "Regular Season" },
    { label: "Week 5", stage: "Regular Season" },
    { label: "Week 6", stage: "Regular Season" },
    { label: "Week 7", stage: "Regular Season" },
    { label: "Week 8", stage: "Regular Season" },
    { label: "Week 9", stage: "Regular Season" },
    { label: "Week 10", stage: "Regular Season" },
    { label: "Week 11", stage: "Regular Season" },
    { label: "Week 12", stage: "Regular Season" },
    { label: "Week 13", stage: "Regular Season" },
    { label: "Week 14", stage: "Regular Season" },
    { label: "Week 15", stage: "Regular Season" },
    { label: "Week 16", stage: "Regular Season" },
    { label: "Week 17", stage: "Regular Season" },
    { label: "Week 18", stage: "Regular Season" },
    { label: "Wild Card", stage: "Post Season" },
    { label: "Divisional Round", stage: "Post Season" },
    { label: "Conference Championships", stage: "Post Season" },
    { label: "Super Bowl", stage: "Post Season" }
];


// useWeekStore stores the selected week & season while also holding two set functions
export const useWeekStore = create((set) => ({
    weekIndex: 0,
    nextWeek: () =>
        set((state) => ({
            weekIndex: Math.min(state.weekIndex + 1, weeks.length - 1),
        })),

    prevWeek: () =>
        set((state) => ({
            weekIndex: Math.max(state.weekIndex - 1, 0),
        })),
    weeks,
}));