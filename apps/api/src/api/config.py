from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field(default="TravelG3n API")
    debug: bool = Field(default=True)
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

def get_settings():
    return Settings()
