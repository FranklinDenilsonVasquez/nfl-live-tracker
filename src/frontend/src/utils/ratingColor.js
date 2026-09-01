// Color bands for Player Game Rating (see CONTEXT.md). Thresholds are a
// starting point, tuned visually once rendered.
export const getRatingColor = (rating) => {
  if (rating == null) return null;
  if (rating < 5) return "#e74c3c"; // red
  if (rating < 7) return "#f1c40f"; // yellow
  return "#2ecc71"; // green
};
