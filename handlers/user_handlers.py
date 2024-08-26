from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
from logging_settings.logging_module import log_incoming_message

router: Router = Router()


@router.message(Command(commands='start'))
async def process_start_command(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer(text=LEXICON_RU['/help'])
