from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# BACKEND_DIR = Path(__file__).parent.parent.parent
BACKEND_DIR = Path(__file__).parents[2]
print("BACKEND_DIR", BACKEND_DIR)

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    LLM_MODEL: str = "gemini-3.5-flash-lite"
    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
print(settings.LLM_MODEL)