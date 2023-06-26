# app/config.py

import os

from pydantic import AnyHttpUrl, BaseSettings, Field, PostgresDsn


class Settings(BaseSettings):
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

    DATABASE_URI: PostgresDsn = Field(..., env="DATABASE_URI")
    
    DEBUG: bool = Field(default=True, env="DEBUG")
    DEBUG_PORT: int = 8080

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = Field([], env="BACKEND_CORS_ORIGINS")
    BACKEND_CORS_ALLOW_ALL: bool = Field(default=False, env="BACKEND_CORS_ALLOW_ALL")
    
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    REFRESH_TOKEN_EXPIRE_MINUTES: int = Field(default=60 * 24 * 7, env="REFRESH_TOKEN_EXPIRE_MINUTES")
    IP_ADDRESS_WHITELIST_ADMIN_PANEL: list[str] = Field(default=[], env="IP_ADDRESS_WHITELIST_ADMIN_PANEL")


settings = Settings()
