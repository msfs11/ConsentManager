"""
Loads configuration
"""

from pydantic import AnyHttpUrl, BaseSettings, Field, PostgresDsn

class Settings(BaseSettings):
    """
    Settings class
    """
    class Config:
        """
        Settings class
        """
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    DATABASE_URI: PostgresDsn = Field(..., env="DATABASE_URI")
    DEBUG: bool = Field(default=True, env="DEBUG")
    DEBUG_PORT: int = 8080

    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: int = Field(..., env="REDIS_PORT")
    REDIS_DB: int = Field(..., env="REDIS_DB")
    REDIS_PASSWORD: str = Field(..., env="REDIS_PASSWORD")
    REDIS_SSL: bool = Field(..., env="REDIS_SSL")

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = Field([], env="BACKEND_CORS_ORIGINS")
    BACKEND_CORS_ALLOW_ALL: bool = Field(default=False, env="BACKEND_CORS_ALLOW_ALL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ADMIN_IP_WHITELIST: list[str] = Field(default=[], env="ADMIN_IP_WHITELIST")


settings = Settings()
