export const calculateImpactScore = (player) => {
    const position = player.position;
    const base_score = 10;

    if (!player.stats || Object.keys(player.stats).length === 0) {
        return base_score;
    }

    switch (position) {
        case "QB":
            return base_score + (
                (player.stats?.passing?.passing_attempted || 0)
                + (player.stats?.passing?.passing_touch_downs || 0 ) * 50
                - (player.stats?.passing?.passing_interceptions || 0) * 30
            );
        case "RB":
            return base_score + (
                (player.stats?.rushing?.rushing_yards || 0) * 1
                + (player.stats?.rushing?.rushing_touchdowns || 0) * 40
                - (player.stats?.fumbles?.total_fumbles || 0) * 30
            );
        case "WR":
            return base_score + (
                (player.stats?.receiving?.receiving_yards || 0) * 1
                + (player.stats?.receiving?.receiving_touchdowns || 0) * 45
                - (player.stats?.fumble?.total_fumbles || 0) * 30
                + (player.stats?.receiving?.total_receptions || 0) * 2
            );
        case "TE":
            return base_score + (
                (player.stats?.receiving?.receiving_yards || 0) * 1
                + (player.stats?.receiving?.receiving_touchdowns || 0) * 45
                - (player.stats?.fumble?.total_fumbles || 0) * 30
                + (player.stats?.receiving?.total_receptions || 0) * 2
            );
        case "CB":
            return base_score + (
                (player.stats?.defense?.tackles || 0) * 0.5
                + (player.stats?.defense?.sacks || 0) * 6
                + (player.stats?.defense?.qb_hits || 0) * 6
                + (player.stats?.defense?.passes_defended || 0) * 5
                + (player.stats?.interception?.total_interceptions || 0) * 25
                + (player.stats?.interception?.intercepted_touch_downs || 0) * 30
                + (player.stats?.fumble?.fumble_recovery || 0) * 8
                + (player.stats?.fumble?.fumble_recovery_td || 0) * 20
                + (player.stats?.defense?.forced_fumbles || 0) * 10
            );
        case "DE":
            return base_score + (
                (player.stats?.defense?.tackles || 0) * 0.7
                + (player.stats?.defense?.sacks || 0) * 15
                + (player.stats?.defense?.tackles_for_loss || 0) * 4
                + (player.stats?.defense?.qb_hits || 0) * 5
                + (player.stats?.defense?.forced_fumbles || 0) * 10
                + (player.stats?.fumble?.fumble_recovery || 0) * 8
                + (player.stats?.fumble?.fumble_recovery_td || 0) * 20
            );
        case "DT":
            return base_score + (
                (player.stats?.defense?.tackles || 0) * 0.7
                + (player.stats?.defense?.sacks || 0) * 15
                + (player.stats?.defense?.tackles_for_loss || 0) * 4
                + (player.stats?.defense?.qb_hits || 0) * 5
                + (player.stats?.defense?.forced_fumbles || 0) * 10
                + (player.stats?.fumble?.fumble_recovery || 0) * 8
                + (player.stats?.fumble?.fumble_recovery_td || 0) * 20
            );
        case "LB":
            return base_score + (
                (player.stats?.defense?.tackles || 0) * 1
                + (player.stats?.defense?.sacks || 0) * 10
                + (player.stats?.defense?.qb_hits || 0) * 3
                + (player.stats?.defense?.passes_defended || 0) * 5
                + (player.stats?.defense?.tackles_for_loss || 0) * 4
                + (player.stats?.interception?.total_interceptions || 0) * 25
                + (player.stats?.interception?.intercepted_touch_downs || 0) * 30
                + (player.stats?.fumble?.fumble_recovery || 0) * 8
                + (player.stats?.fumble?.fumble_recovery_td || 0) * 20
                + (player.stats?.defense?.forced_fumbles || 0) * 10
            );
        case "S":
            return base_score + (
                (player.stats?.defense?.tackles || 0) * 0.8
                + (player.stats?.defense?.sacks || 0) * 8
                + (player.stats?.defense?.qb_hits || 0) * 3
                + (player.stats?.defense?.passes_defended || 0) * 5
                + (player.stats?.interception?.total_interceptions || 0) * 25
                + (player.stats?.interception?.intercepted_touch_downs || 0) * 30
                + (player.stats?.fumble?.fumble_recovery || 0) * 8
                + (player.stats?.fumble?.fumble_recovery_td || 0) * 20
                + (player.stats?.defense?.forced_fumbles || 0) * 10
            );

    }
}