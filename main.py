import asyncio
import logging.config
import yaml
import os

from aiogram import Bot, Dispatcher
from config.config import Config, load_config
from handlers import other_handlers, user_handlers
from middlewares import outer
from notifications.notifications import schedule_messages


def setup_logging() -> None:
    config_path = os.path.join('logging_settings', 'logging_config.yaml')

    try:
        with open(config_path, 'rt') as f:
            log_config = yaml.safe_load(f.read())
        logging.config.dictConfig(log_config)
    except Exception as e:
        logging.basicConfig(level=logging.WARN)
        logging.error("Error at logging config load: %s", e)


setup_logging()
logger = logging.getLogger(__name__)


async def main() -> None:
    # Configuration load
    logger.info("Configuration load...")
    config: Config = load_config()

    # Bot initialization
    logger.info("Bot initialization...")
    bot: Bot = Bot(token=config.tg_bot.bot_token)
    dp: Dispatcher = Dispatcher()

    # Registration of routers in dispatcher
    logger.info("Registration of router 'user_handlers'...")
    dp.include_router(user_handlers.router)
    logger.info("Registration of router 'other_handlers'...")
    dp.include_router(other_handlers.router)

    # Registration of middlewares
    logger.info("Registration of middleware 'CheckUserIdMiddleware'...")
    dp.update.middleware(outer.CheckUserIdMiddleware())

    # Start of scheduler
    logger.info("Start of scheduler...")
    schedule_messages()

    # Skip of accumulated updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
