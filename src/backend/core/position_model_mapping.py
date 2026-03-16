from src.backend.models.player_stats import (QBStats, SkillStats, DefenseStats, KickerStats, PunterStats,
                                             KickReturnerStats, PuntReturnerStats)

POSITION_MODEL_MAP = {
    "QB": QBStats,
    "RB": SkillStats,
    "FB": SkillStats,
    "WR": SkillStats,
    "TE": SkillStats,
    "DE": DefenseStats,
    "DT": DefenseStats,
    "LB": DefenseStats,
    "CB": DefenseStats,
    "S": DefenseStats,
    "DB": DefenseStats,
    "PK": KickerStats,
    "P": PunterStats,
    "KR": KickReturnerStats,
    "PR": PuntReturnerStats,
}