from src.backend.services.standing_service import get_season_standings

if __name__ == "__main__":
    result = get_season_standings(4)
    print(result)