import logging

from aiogram import Router
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
from logging_settings.logging_module import log_incoming_message
from db.database import set_user_state

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer(text=LEXICON_RU['/start'])
    await set_user_state(state=True)


@router.my_chat_member()
async def my_chat_member_handler(my_chat_member: ChatMemberUpdated):
    logger.error(f"User blocked the bot")

    if my_chat_member.chat.type == 'private':
        if my_chat_member.new_chat_member.status == 'kicked':
            await set_user_state(state=False)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer(text=LEXICON_RU['/help'])
