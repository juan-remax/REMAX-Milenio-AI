from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    allowed_user_ids: list[int]
    github_token: str = ""
    github_repo: str = "juan-remax/REMAX-Milenio-AI"
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/remax_milenio"
    app_name: str = "REMAX Milenio AI"
    debug: bool = True

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
