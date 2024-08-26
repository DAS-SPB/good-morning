import logging

from aiogram.types import Message

logger = logging.getLogger(__name__)


def log_incoming_message(message: Message, loglevel: str = 'debug'):
    loglevel_map = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    loglevel_value = loglevel_map.get(loglevel.lower(), logging.DEBUG)

    logger.log(
        loglevel_value,
        f"Received message: from_user.username: {message.from_user.username}, text: {message.text}, "
        f"is_photo: {bool(message.photo)}, is_sticker: {bool(message.sticker)}, is_video: {bool(message.video)},"
        f"is_voice: {bool(message.voice)}"
    )
