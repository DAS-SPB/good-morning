import logging

from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User
from lexicon.lexicon import LEXICON_RU
from config.config import Config, load_config

config: Config = load_config()
main_user_id = int(config.tg_bot.main_user_id)

logger = logging.getLogger(__name__)


class CheckUserIdMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        print(data)
        user: User = data.get('event_from_user')
        bot = data.get('bot')

        logger.info(f"Middleware, user: {user}, user.id: {user.id}")

        if not user.id == main_user_id:
            logger.info(f"Message from unknown user. User: id={user.id}, username={user.username}")
            try:
                await bot.send_message(chat_id=user.id, text=LEXICON_RU['unknown_user'])
            except Exception as e:
                logger.error(f"Failed to send message to user {user.id}: {e}")
            return

        return await handler(event, data)
