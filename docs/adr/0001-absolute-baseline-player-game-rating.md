# Absolute, baseline-6.0 Player Game Rating instead of a relative/percentile one

Player Game Rating (see `CONTEXT.md`) is computed as an absolute, position-weighted formula seeded at 6.0, not as a percentile or z-score against other players at the same position for that week.

A relative rating is self-normalizing across wildly different stat scales (yards vs. tackles vs. completion %) and would have been the more "statistically obvious" choice, but the feature is meant to answer "how is this player playing in this game," modeled after live sports-app match ratings (Sofascore/WhoScored-style) that start a player at a neutral baseline and move up or down based on their own actions - not "how does this player compare to others." A relative rating for cross-player/league comparison is a distinct, deliberately deferred feature (see "League Percentile Rating" in `CONTEXT.md`).

Ratings are precomputed via ETL and persisted per (player, game), rather than computed on demand, for performance at scale; the ratings table is treated as an idempotently re-derivable cache, recomputed if the underlying game stats are ever corrected.
