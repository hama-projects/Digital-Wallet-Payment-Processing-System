from pydantic import BaseModel


class Wallet(BaseModel):
    user_id: int
    balance: float