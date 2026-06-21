from pydantic import BaseModel


class Reward(BaseModel):
    user_id: int
    points: int