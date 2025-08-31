from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    app_name: str = "Expense Tracker API"
    debug: bool = False

    # Database
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/expense_tracker"

    # Pydantic-settings config
    model_config = SettingsConfigDict(
        env_file=".env",          # read from .env in local dev
        env_file_encoding="utf-8",
        case_sensitive=False,     # allows MONZO_CLIENT_ID vs monzo_client_id
    )

# singleton settings object
settings = Settings()
