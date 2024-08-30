import logging

from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from config.config import Config, load_config
from db.database import get_user_state, get_chat_id
from external_api.cats import get_cat_image

logger = logging.getLogger(__name__)

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.bot_token)

scheduler: AsyncIOScheduler = AsyncIOScheduler()


async def send_scheduled_message(user_state: bool, chat_id: int) -> None:
    if user_state and chat_id:
        try:
            text = await get_cat_image()
            await bot.send_message(chat_id=chat_id, text=text)

            logger.info(f"Bot sent message to the chat_id: {chat_id}")
        except Exception as e:
            logger.error(f"Bot can't sent message to the chat_id: {chat_id}: {e}")


async def scheduled_job() -> None:
    user_state = await get_user_state()
    chat_id = await get_chat_id()

    await send_scheduled_message(user_state=user_state, chat_id=chat_id)


def schedule_messages() -> None:
    scheduler.add_job(
        scheduled_job,
        trigger=CronTrigger(second=30),
    )
    scheduler.start()
