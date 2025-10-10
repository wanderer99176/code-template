from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """加载并验证应用程序设置。"""
    DATABASE_URL: str = "sqlite:///./test.db"
    
    # 从 .env 文件加载设置
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
