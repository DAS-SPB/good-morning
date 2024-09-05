from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database_url: str


@dataclass
class BotConfig:
    bot_token: str
    main_user_id: str
    main_user_bd: str


@dataclass
class ExtAPIConfig:
    cat_api_key: str
    openai_api_key: str


@dataclass
class Config:
    tg_bot: BotConfig
    db: DatabaseConfig
    ext_api: ExtAPIConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=BotConfig(
            bot_token=env('BOT_TOKEN'),
            main_user_id=env('MAIN_USER_ID'),
            main_user_bd=env('MAIN_USER_BD')
        ),
        db=DatabaseConfig(
            database_url=env('DATABASE_URL')
        ),
        ext_api=ExtAPIConfig(
            cat_api_key=env('CAT_API_KEY'),
            openai_api_key=env('OPENAI_API_KEY')
        )
    )
