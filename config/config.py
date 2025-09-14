from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
import pathlib


ROOT_DIR = pathlib.Path(__file__).parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    BOT_API: SecretStr

    DB_USER: str
    DB_PASS: str
    DB_PORT: int
    DB_HOST: str
    DB_NAME: str
    
    POSTGRES_URL: str
    DATABASE_URL: str
    
    ENCRYPT_KEY: SecretStr
    DEBUG: bool = False

    @property
    def get_database_url(self):
        return settings.DATABASE_URL

settings = Settings() # noqa
