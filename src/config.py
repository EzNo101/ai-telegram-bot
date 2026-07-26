from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    OPENROUTER_API_KEY: str
    MODEL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()  # type: ignore
