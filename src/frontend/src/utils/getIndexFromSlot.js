export const getIndexFromSlot = (id) => {
    const match = id.match(/\d+/)
    return match ? parseInt(match[0], 10) - 1: 0;
};