export const findPlayerTeam = (rosters, selectedId) => {
    const home = rosters?.home?.find((p) => p.player_id === selectedId);
    if (home) return {team: "home"};

    const away = rosters?.away?.find((p) => p.player_id === selectedId);
    if (away) return {team: "away"};

    return null;
}