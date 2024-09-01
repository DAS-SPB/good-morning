from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone

from db.database import get_user_state, get_chat_id
from notifications.notifications import send_scheduled_message

scheduler: AsyncIOScheduler = AsyncIOScheduler()


async def scheduled_job() -> None:
    user_state = await get_user_state()
    chat_id = await get_chat_id()

    await send_scheduled_message(user_state=user_state, chat_id=chat_id)


def schedule_messages() -> None:
    scheduler.add_job(
        scheduled_job,
        trigger=CronTrigger(hour=10, timezone=timezone('Europe/Moscow')),
    )
    scheduler.start()
