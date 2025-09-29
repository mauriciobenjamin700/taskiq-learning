from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings.

    Attributes:
        DB_URL (str): Database connection URL.
    """

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=True
    )

    DB_URL: str = "sqlite+aiosqlite:///./test.db"


settings = Settings()
