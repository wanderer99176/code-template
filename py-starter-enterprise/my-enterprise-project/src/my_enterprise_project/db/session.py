from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from my_enterprise_project.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """获取数据库会话的依赖项。"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
