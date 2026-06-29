from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    allowed_user_ids: list[int] = []
    github_token: str = ""
    github_repo: str = "juan-remax/REMAX-Milenio-AI"
    database_url: str = "sqlite+aiosqlite:///data/remax_milenio.db"
    app_name: str = "REMAX Milenio AI"
    debug: bool = True

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}

    @field_validator("allowed_user_ids", mode="before")
    @classmethod
    def parse_allowed_user_ids(cls, v):
        if isinstance(v, str):
            import json
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return [int(x.strip()) for x in v.split(",") if x.strip()]
        if isinstance(v, int):
            return [v]
        return v or []


settings = Settings()
