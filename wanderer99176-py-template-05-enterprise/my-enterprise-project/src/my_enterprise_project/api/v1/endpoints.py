from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from my_enterprise_project.db.session import get_db

router = APIRouter()


@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    """健康检查端点。"""
    # 检查数据库连接的简单方法
    db.execute("SELECT 1")
    return {"status": "ok"}
