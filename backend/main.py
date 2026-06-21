from fastapi import FastAPI

from backend.api.routes_auth import router as auth_router
from backend.api.routes_wallet import router as wallet_router
from backend.api.routes_transactions import router as transaction_router
from backend.api.routes_rewards import router as rewards_router
from backend.api.routes_admin import router as admin_router

app = FastAPI(title="FinTech Wallet & Payment System")


@app.get("/")
def root():
    return {"message": "FinTech Wallet API running"}


app.include_router(auth_router)
app.include_router(wallet_router)
app.include_router(transaction_router)
app.include_router(rewards_router)
app.include_router(admin_router)