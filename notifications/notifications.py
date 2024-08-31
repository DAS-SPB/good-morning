import logging
import random

from aiogram import Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, MessageEntity

from config.config import Config, load_config
from external_api.cats import get_cat_image
from db.database import get_num_of_phrases, get_phrase
from lexicon.lexicon import LEXICON_RU

logger = logging.getLogger(__name__)

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.bot_token)

more_button = InlineKeyboardButton(
    text=LEXICON_RU.get('more_button'),
    callback_data='more_button_pressed'
)

keyboard = InlineKeyboardMarkup(inline_keyboard=[[more_button]])


async def get_random_id() -> int:
    current_phrase_id = random.randint(1, await get_num_of_phrases())
    return current_phrase_id


async def send_scheduled_message(user_state: bool, chat_id: int) -> None:
    if user_state and chat_id:
        try:
            cat_image = await get_cat_image()
            gm_phrase = await get_phrase(phrase_id=await get_random_id())

            # return default gif in case of error on the CatAPI side
            if cat_image.startswith('http'):
                await bot.send_photo(
                    chat_id=chat_id,
                    photo=cat_image,
                    caption=gm_phrase,
                    caption_entities=[MessageEntity(type='spoiler', offset=0, length=len(gm_phrase))],
                    message_effect_id='5159385139981059251',
                    reply_markup=keyboard
                )

                logger.info(f"Bot sent message to the chat_id: {chat_id}")

            else:
                await bot.send_document(
                    chat_id=chat_id,
                    document=cat_image,
                    caption=gm_phrase,
                    caption_entities=[MessageEntity(type='spoiler', offset=0, length=len(gm_phrase))],
                    message_effect_id='5159385139981059251',
                    reply_markup=keyboard
                )

                logger.error(f"Bot sent message with default gif to the chat_id: {chat_id}")

        except Exception as e:
            logger.error(f"Bot can't sent message to the chat_id: {chat_id}: {e}")
