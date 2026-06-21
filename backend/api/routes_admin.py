from fastapi import APIRouter
from backend.analytics.dashboard_data import get_dashboard_summary
from backend.analytics.metrics import transaction_success_rate

router = APIRouter()


@router.get("/admin/dashboard")
def admin_dashboard():
    summary = get_dashboard_summary()
    success_rate = transaction_success_rate()

    return {
        "summary": summary,
        "transaction_success_rate": success_rate,
    }