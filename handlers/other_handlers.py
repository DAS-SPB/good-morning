import logging

from aiogram import Router, F
from aiogram.types import Message, ContentType, CallbackQuery, InputMediaPhoto, InputMediaAnimation
from lexicon.lexicon import LEXICON_RU
from external_api.cats import get_cat_image
from logging_settings.logging_module import log_incoming_message

router: Router = Router()
logger = logging.getLogger(__name__)


@router.callback_query(F.data == 'more_button_pressed')
async def update_image(callback: CallbackQuery):
    log_incoming_message(message=callback.message, loglevel='info')

    cat_image = await get_cat_image()

    # return default gif in case of error on the CatAPI side
    if cat_image.startswith('http'):
        await callback.message.edit_media(
            media=InputMediaPhoto(media=cat_image, caption=LEXICON_RU.get('more_button_pressed')),
            reply_markup=callback.message.reply_markup
        )
    else:
        await callback.message.edit_media(
            media=InputMediaAnimation(media=cat_image, caption=LEXICON_RU.get('more_button_pressed')),
            reply_markup=callback.message.reply_markup
        )


@router.message(F.content_type == ContentType.PHOTO)
async def reply_for_photo(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_photo(
        photo='AgACAgIAAxkBAAPUZtN8yUebDh9fDuyJKkUL_ab3PXgAAvzsMRutuJhK1MmwO8MEkZYBAAMCAAN5AAM1BA')


@router.message(F.content_type == ContentType.STICKER)
async def reply_for_sticker(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_sticker(
        sticker='CAACAgIAAxkBAAPeZtN-9lP4yNqRZvmFZbrQOWNgRzMAAg8VAAJQAAE5SLTQjX7JrCC6NQQ')


@router.message()
async def reply_for_any_other_messages(message: Message):
    log_incoming_message(message=message, loglevel='info')

    await message.answer_document(
        document='BQACAgIAAxkBAAPgZtOAjpflCJCQxvq9ElSkIWNVdoAAAuZUAAJeZqBKRQIn_UfIMRM1BA')
