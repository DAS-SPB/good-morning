from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class BotConfig:
    bot_token: str
    admin_ids: list[int]
    main_user_id: str
    main_user_bd: str


@dataclass
class ExtAPIConfig:
    cat_api_key: str


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
            admin_ids=list(map(int, env.list('ADMIN_IDS'))),
            main_user_id=env('MAIN_USER_ID'),
            main_user_bd=env('MAIN_USER_BD')
        ),
        db=DatabaseConfig(
            database=env('DATABASE'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        ),
        ext_api=ExtAPIConfig(
            cat_api_key=env('CAT_API_KEY')
        )
    )
