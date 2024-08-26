import logging

from aiogram import Router, F
from aiogram.types import Message, ContentType
from lexicon.lexicon import LEXICON_RU
from logging_module.logging_module import log_incoming_message

logger = logging.getLogger(__name__)

router: Router = Router()


@router.message(F.content_type == ContentType.PHOTO)
async def send_photo_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_photo(photo=message.photo[-1].file_id)


@router.message(F.content_type == ContentType.STICKER)
async def send_sticker_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_sticker(sticker=message.sticker.file_id)


@router.message()
async def send_text_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
