"""Configuration settings."""
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_ignore_empty=True)

    pageindex_api_key: str
    openai_api_key: str

    openai_model: str = "gpt-4o-mini"
    request_timeout: int = 60
    max_retries: int = 3
    log_level: str = "INFO"


settings = Settings()

