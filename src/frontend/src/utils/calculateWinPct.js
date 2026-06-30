export function calculateWinPct(wins, losses, ties) {
  const gamesPlayed = wins + losses + ties;

  if (gamesPlayed === 0) return "0.000";

  return ((wins + ties * 0.5) / gamesPlayed).toFixed(3);
}
