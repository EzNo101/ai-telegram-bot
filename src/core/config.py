from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    OPENROUTER_API_KEY: str
    MODEL: str

    # Database
    DB_URL: str
    DB_POOL_SIZE: int
    DB_POOL_RECYCLE: int
    DB_POOL_TIMEOUT: int
    DB_PRE_PING: bool

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
