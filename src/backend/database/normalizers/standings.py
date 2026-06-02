from .utils import parse_record
from src.backend.database.repositories.season_repository import get_season_id

def normalize_standing_stats(cursor, raw_data):
    normalized = []

    for team in raw_data:
        conference_wins, conference_losses = parse_record(team["records"]["conference"])
        division_wins, division_losses = parse_record(team["records"]["division"])
        home_wins, home_losses = parse_record(team["records"]["home"])
        road_wins, road_losses = parse_record(team["records"]["road"])
        season_id = get_season_id(cursor=cursor, season_year=team["league"]["season"])

        normalized.append({
            "season_id" : season_id,
            "team_id" : team["team"]["id"],
            "conference" : team["conference"],
            "division" : team["division"],
            "position" : team["position"],
            "wins" : team["won"],
            "losses" : team["lost"],
            "ties" : team["ties"],
            "points_for" : team["points"]["for"],
            "points_against" : team["points"]["against"],
            "point_differential" : team["points"]["difference"],
            "conference_wins" : conference_wins,
            "conference_losses" : conference_losses,
            "division_wins" : division_wins,
            "division_losses" : division_losses,
            "home_wins" : home_wins,
            "home_losses" : home_losses,
            "road_wins" : road_wins,
            "road_losses" : road_losses,
            "streak" : team["streak"]
        })

    return normalized