from pydantic import BaseModel

class PassingStats(BaseModel):
    passing_attempted: int | None = 0
    passing_completion: int | None = 0
    passing_average: float | None = 0
    passing_yards: int | None = 0
    passing_touchdowns: int | None = 0
    passing_interceptions: int | None = 0

class RushingStats(BaseModel):
    total_rushes: int | None = 0
    rushing_yards: int | None = 0
    rushing_average: float | None = 0
    rushing_touchdowns: int | None = 0

class FumbleStats(BaseModel):
    total_fumbles: int | None = 0
    fumble_lost: int | None = 0

class ReceivingStats(BaseModel):
    receiving_targets: int | None = 0
    total_receptions: int | None = 0
    receiving_yards: int | None = 0
    receiving_average: float | None = 0
    receiving_touchdowns: int | None = 0

class DefenseDetails(BaseModel):
    tackles: int | None = 0
    unassisted_tackles: int | None = 0
    sacks: int | None = 0
    tackles_for_loss: int | None = 0
    passes_defended: int | None = 0
    qb_hits: int | None = 0

class InterceptionStats(BaseModel):
    total: int | None = 0
    yards: int | None = 0
    touchdowns: int | None = 0

class QBStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Passing stats
    passing: PassingStats
    # Rushing stats
    rushing: RushingStats
    # Fumble stats
    fumbles: FumbleStats


class SkillStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Receiving stats
    receiving: ReceivingStats
    # Rushing stats
    rushing: RushingStats
    # Fumble stats
    fumbles: FumbleStats

class DefenseStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Defensive stats
    defense: DefenseDetails
    interception: InterceptionStats
    fumbles: FumbleStats

class KickerStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    fg_made: int
    fg_attempted: int
    fg_percentage: float
    long: int
    xp_made: int
    xp_attempted: int
    points: int
    field_goals_from_1_19_yards: int | None = 0
    field_goals_from_20_29_yards: int | None = 0
    field_goals_from_30_39_yards: int | None = 0
    field_goals_from_40_49_yards: int | None = 0
    field_goals_from_50_yards: int | None = 0

class PunterStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    punt_total: int
    punt_yards: int
    punt_average: float
    touchbacks: int
    inside_20: int
    long_punt: int

class KickReturnerStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    total_kick_returns: int
    kick_return_yards: int
    kick_return_average: float
    kick_return_long: int
    td: int
    kick_return_td: int

class PuntReturnerStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    total: int
    yards: int
    average: float
    long: int
    touchdown: int

