"""
module for the project configuration
"""
from pathlib import Path

from pydantic import Field, ConfigDict, SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Project configuration class"""
    PROJECT_PATH: str = str(Path(__file__).parent.parent)
    API_KEY: SecretStr
    BASE_URL: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER: str
    PGPASSWORD: str
    ENVIRONMENT: str

    model_config = ConfigDict(
        env_ignore_empty=True,
        extra="ignore",
    )

settings = Settings()
