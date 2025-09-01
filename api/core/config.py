from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    app_name: str = "Expense Tracker API"
    debug: bool = False

    api_domain: str = "http://localhost:8000"
    website_domain: str = "http://localhost:3000"

    supertokens_connection_uri: str = ""
    supertokens_api_key: str = ""

    google_client_id: str = ""
    google_client_secret: str = ""

    # Database
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "expense_tracker"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://{quote_plus(self.db_user)}:{quote_plus(self.db_password)}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

# singleton settings object
settings = Settings()
