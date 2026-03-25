from pydantic import BaseModel
from typing import Optional, List

class PassingStats(BaseModel):
    passing_attempted: int | None = 0
    passing_completion: int | None = 0
    passing_average: float | None = 0
    passing_yards: int | None = 0
    passing_touchdowns: int | None = 0
    passing_interceptions: int | None = 0

# For QB position
class RushingStats(BaseModel):
    total_rushes: int | None = 0
    rushing_yards: int | None = 0
    rushing_average: float | None = 0
    rushing_touchdowns: int | None = 0

class RushingDetails(BaseModel):
    total_rushes: int | None = 0
    rushing_yards: int | None = 0
    rushing_average: float | None = 0
    rushing_touchdowns: int | None = 0
    longest_rush: int | None = 0
    two_point_rushes: int | None = 0
    kick_return_touchdowns: int | None = 0
    exp_return_touchdowns: int | None = 0

class FumbleStats(BaseModel):
    total_fumbles: int | None = 0
    fumble_lost: int | None = 0
    fumble_recovery: int | None = 0
    fumble_recovery_td: int | None = 0

class FumbleDetails(BaseModel):
    total_fumbles : int | None = 0
    fumble_lost : int | None = 0
    fumble_recovery : int | None = 0
    fumble_recovery_td : int | None = 0

class ReceivingStats(BaseModel):
    receiving_targets: int | None = 0
    total_receptions: int | None = 0
    receiving_yards: int | None = 0
    receiving_average: float | None = 0
    receiving_touchdowns: int | None = 0
    longest_reception: int | None = 0
    two_point_receptions: int | None = 0

class DefenseDetails(BaseModel):
    tackles: int | None = 0
    unassisted_tackles: int | None = 0
    sacks: int | None = 0
    tackles_for_loss: int | None = 0
    passes_defended: int | None = 0
    qb_hits: int | None = 0

class InterceptionStats(BaseModel):
    total_interceptions: int | None = 0
    yards: int | None = 0
    intercepted_touch_downs: int | None = 0

class KickingStats(BaseModel):
    fg_made: int
    fg_attempted: int
    fg_percentage: float
    fg_long: int
    xp_made: int
    xp_attempted: int
    points: int
    field_goals_from_1_19_yards: int | None = 0
    field_goals_from_20_29_yards: int | None = 0
    field_goals_from_30_39_yards: int | None = 0
    field_goals_from_40_49_yards: int | None = 0
    field_goals_from_50_yards: int | None = 0

class KickingGameStats(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    home_team_score: int
    away_team_score: int
    kicking : Optional[KickingStats] = None

class KickingStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    games : List[KickingGameStats]

class PuntingStats(BaseModel):
    punt_total: int
    punt_yards: int
    punt_average: float
    touchbacks: int
    inside_20: int
    long_punt: int

class KickReturnStats(BaseModel):
    total_kick_returns: int
    kick_return_yards: int
    kick_return_average: float
    kick_return_long: int
    td: int
    kick_return_td: int
    exp_return_td: float

class PuntReturnStats(BaseModel):
    punt_return_total: int
    punt_return_yards: int
    punt_return_average: float
    punt_return_long: int
    punt_return_touchdowns: int

# Nested model for QB per game stats
class QBGameStats(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    home_team_score : int
    away_team_score : int
    passing : Optional[PassingStats] = None
    rushing : Optional[RushingStats] = None
    fumbles: Optional[FumbleStats] = None

# Nested model for the top level QB json response
class QBStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # QB Stats
    games: List[QBGameStats]

# Season long QB stats
class QBStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # QB Stats
    # Passing stats
    passing: PassingStats
    # Rushing stats
    rushing: RushingStats
    # Fumble stats
    fumbles: FumbleStats

# Season long skill position stats
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

# Nested model for the top level Skill position json response
class SkillGameStats(BaseModel):
    game_id : int
    home_team : str
    away_team : str
    home_team_score : int
    away_team_score : int
    receiving : Optional[ReceivingStats] = None
    rushing : Optional[RushingStats] = None
    fumbles : Optional[FumbleStats] = None

# Nested model for QB per game stats
class SkillStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Skill position stats
    games: List[SkillGameStats]

# season long defense stats
class DefenseStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Defensive stats
    defense: DefenseDetails
    int_stats: InterceptionStats
    fumbles: FumbleStats

class DefenseGameStats(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    home_team_score: int
    away_team_score: int
    defense: Optional[DefenseDetails] = None
    int_stats: Optional[InterceptionStats] = None
    fumbles: Optional[FumbleStats] = None

class DefenseStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    games : List[DefenseGameStats]

# season long kicker stats
class KickerStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Kicker stats
    kicking : KickingStats

class PunterGameStats(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    home_team_score: int
    away_team_score: int
    punting : Optional[PuntingStats] = None

class PunterStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    games: List[PunterGameStats]

# season long punter stats
class PunterStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Punting stats
    punting: PuntingStats

# season long kick returner stats
class KickReturnerStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    kicking : KickingStats

# season long punt returner stats
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

class LinemenStats(BaseModel):
    player_id: int
    player_name: str
    season_id: int | None = 0
    position: str
    player_img: str
    fumbles : FumbleStats
    defense : DefenseDetails

class LinemanGameStats(BaseModel):
    game_id: int
    home_team: str
    away_team: str
    home_team_score: int
    away_team_score: int
    fumbles : Optional[FumbleDetails] = None
    defense : Optional[DefenseDetails] = None

class LinemanStatsPerGame(BaseModel):
    player_id: int
    player_name: str
    season_id: int
    position: str
    player_img: str
    # Game stats
    games : List[LinemanGameStats]
