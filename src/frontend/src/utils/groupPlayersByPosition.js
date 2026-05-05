export const groupPlayersByPosition = (players = []) => {
    return players.reduce((list, player) => {
        const position = player.position || "UNKNOWN";

        if (!list[position]) {
            list[position] = [];
        }
        list[position].push(player);

        return list

        }, {});
    };