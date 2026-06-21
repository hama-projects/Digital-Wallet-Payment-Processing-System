import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/fintech_wallet"
)

SECRET_KEY = "supersecretkey"

FRAUD_LIMIT = 10000