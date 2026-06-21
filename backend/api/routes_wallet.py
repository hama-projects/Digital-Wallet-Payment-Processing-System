from fastapi import APIRouter
from backend.services.wallet_service import get_balance, deposit_money

router = APIRouter()


@router.get("/wallet/{user_id}")
def wallet_balance(user_id: int):
    balance = get_balance(user_id)
    return {"user_id": user_id, "balance": balance}


@router.post("/wallet/deposit")
def deposit(user_id: int, amount: float):
    new_balance = deposit_money(user_id, amount)
    return {"message": "Deposit successful", "balance": new_balance}