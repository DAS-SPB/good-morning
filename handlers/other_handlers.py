from aiogram import Router, F
from aiogram.types import Message, ContentType
from lexicon.lexicon import LEXICON_RU
from external_api import cats
from logging_settings.logging_module import log_incoming_message

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

    cat_image_url = await cats.get_cat_image()

    await message.answer(text=cat_image_url)
