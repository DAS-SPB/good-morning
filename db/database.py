import logging

from pymongo.results import InsertManyResult, UpdateResult

from db.connection import user_data, phrases

logger = logging.getLogger(__name__)


# was used to fill MongoDB with phrases
# phrases_to_db = {
#     "1": "Example 1",
#     "2": "Example 2"
# }


async def set_user_data(state: bool, chat_id: int, user_id=1, collection=user_data) -> UpdateResult:
    query = {
        "user_id": user_id
    }
    try:
        result: UpdateResult = await collection.update_one(
            filter=query,
            update={"$set": {"is_active": state, "chat_id": chat_id}},
            upsert=True
        )
        logger.info(
            f"MongoDB. User data updated, state={state}")
    except Exception as e:
        logger.error(f"MongoDB. User data update failed: {e}")
        raise Exception

    return result


async def get_user_state(user_id=1, collection=user_data) -> bool:
    try:
        current_user_state = await collection.find_one({"user_id": user_id})
        if current_user_state:
            logger.info(f"MongoDB. Current user state: {current_user_state.get('is_active')}")

            return current_user_state.get('is_active')
    except Exception as e:
        logger.error(f"MongoDB. Current user state can't be fetched: {e}")
        raise Exception

    return False


async def get_chat_id(user_id=1, collection=user_data) -> int:
    try:
        current_chat_id = await collection.find_one({"user_id": user_id})
        if current_chat_id:
            logger.info(f"MongoDB. Current chat_id: {current_chat_id.get('chat_id')}")

            return current_chat_id.get('chat_id')
    except Exception as e:
        logger.error(f"MongoDB. Current chat_id can't be fetched: {e}")
        raise Exception

    return False


# was used to fill MongoDB with phrases
# async def insert_phrases(collection=phrases) -> InsertManyResult:
#     payload = [{"phrase_id": int(phrase_id), "phrase": phrase} for phrase_id, phrase in phrases_to_db.items()]
#     try:
#         inserted_data = await collection.insert_many(payload)
#         logger.info(f"MongoDB. Inserted {len(inserted_data.inserted_ids)} phrases into the 'Phrase' collection.")
#     except Exception as e:
#         logger.error(f"MongoDB. Phrases can't be inserted: {e}")
#         raise Exception
#
#     return inserted_data


async def get_phrase(phrase_id: int, collection=phrases) -> str:
    try:
        fetched_phrase = await collection.find_one({"phrase_id": phrase_id})
        if fetched_phrase:
            return fetched_phrase.get('phrase')
    except Exception as e:
        logger.error(f"MongoDB. Phrases can't be fetched: {e}")
        raise Exception

    return "Failed to fetch phrase from DB. Please, connect to administrator"


async def get_num_of_phrases(collection=phrases) -> int:
    try:
        num_of_phrases = await collection.count_documents({})
        if num_of_phrases:
            return num_of_phrases
    except Exception as e:
        logger.error(f"MongoDB. Phrases can't be counted: {e}")
        raise Exception

    # '1' returned as default id of phrase in case of unexpected exceptions
    return 1
