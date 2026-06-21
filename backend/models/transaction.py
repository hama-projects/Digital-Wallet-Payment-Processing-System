from pydantic import BaseModel


class Transaction(BaseModel):
    sender_id: int
    receiver_id: int
    amount: float
    status: str