from fastapi import APIRouter
from backend.services.rewards_engine import get_user_points, add_reward_points

router = APIRouter()


@router.get("/rewards/{user_id}")
def check_rewards(user_id: int):
    points = get_user_points(user_id)
    return {"user_id": user_id, "points": points}


@router.post("/rewards/add")
def add_points(user_id: int, points: int):
    updated = add_reward_points(user_id, points)
    return {"message": "Points added", "points": updated}