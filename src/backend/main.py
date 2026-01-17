from fastapi import FastAPI
from src.backend.api.routes.players import router as player_router

app = FastAPI(
    title="NFL Stats API",
    description="API for fetching NFL teams and players",
    version="1.0.0"
)

# Include routes
app.include_router(player_router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "NFL Stats API is running!"}