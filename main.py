import asyncio
import logging.config
import yaml
import os

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import other_handlers, user_handlers
from middlewares import outer, inner


def setup_logging():
    config_path = os.path.join('logging_settings', 'logging_config.yaml')

    try:
        with open(config_path, 'rt') as f:
            log_config = yaml.safe_load(f.read())
        logging.config.dictConfig(log_config)
    except Exception as e:
        logging.basicConfig(level=logging.WARN)
        logging.error("Ошибка загрузки конфигурации логгирования: %s", e)


setup_logging()
logger = logging.getLogger(__name__)


async def main() -> None:
    logger.info("Загрузка конфигурации...")
    config: Config = load_config()

    logger.info("Инициализация бота...")
    bot = Bot(token=config.tg_bot.bot_token)
    dp = Dispatcher()

    # Регистриуем роутеры в диспетчере
    logger.info("Регистрация роутера 'user_handlers'...")
    dp.include_router(user_handlers.router)
    logger.info("Регистрация роутера 'other_handlers'...")
    dp.include_router(other_handlers.router)

    # Регистриуем middlewares
    logger.info("Регистрация middleware 'CheckUserIdMiddleware'...")
    dp.update.middleware(outer.CheckUserIdMiddleware())

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
