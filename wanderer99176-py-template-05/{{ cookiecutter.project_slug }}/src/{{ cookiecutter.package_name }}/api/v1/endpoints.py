from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from {{ cookiecutter.package_name }}.db.session import get_db

router = APIRouter()


@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint."""
    # A simple way to check DB connection
    db.execute("SELECT 1")
    return {"status": "ok"}
