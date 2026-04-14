from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.backend.api.routes.players import router as player_router
from src.backend.api.routes.teams import router as team_router
from src.backend.api.routes.games import router as game_router
app = FastAPI(
    title="NFL Stats API",
    description="API for fetching NFL teams and players",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(player_router)
app.include_router(team_router)
app.include_router(game_router)
# Root endpoint
@app.get("/")
def root():
    return {"message": "NFL Stats API is running!"}