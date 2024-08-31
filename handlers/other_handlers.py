import logging

from aiogram import Router, F
from aiogram.types import Message, ContentType, CallbackQuery, InputMediaPhoto
from lexicon.lexicon import LEXICON_RU
from external_api.cats import get_cat_image
from logging_settings.logging_module import log_incoming_message

router: Router = Router()
logger = logging.getLogger(__name__)


@router.message(F.content_type == ContentType.PHOTO)
async def send_photo_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_photo(photo=message.photo[-1].file_id)


@router.message(F.content_type == ContentType.STICKER)
async def send_sticker_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_sticker(sticker=message.sticker.file_id)


@router.callback_query(F.data == 'more_button_pressed')
async def update_image(callback: CallbackQuery):
    log_incoming_message(message=callback.message, loglevel='info')

    cat_image = await get_cat_image()

    await callback.message.edit_media(
        media=InputMediaPhoto(media=cat_image, caption=LEXICON_RU.get('more_button_pressed')),
        reply_markup=callback.message.reply_markup
    )


@router.message()
async def send_text_echo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    cat_image_url = await get_cat_image()

    await message.answer(text=cat_image_url)
