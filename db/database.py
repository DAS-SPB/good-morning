import logging

from pymongo.results import InsertManyResult, UpdateResult

from db.connection import user_state, phrases

logger = logging.getLogger(__name__)


# Was used to fill MongoDB with phrases
# phrases_to_db = {
#     "1": "Example 1",
#     "2": "Example 2"
# }


async def set_user_state(state: bool, collection=user_state) -> UpdateResult:
    query = {
        "user_id": 1
    }
    try:
        result: UpdateResult = await collection.update_one(
            filter=query,
            update={"$set": {"is_active": state}},
            upsert=True
        )
        logger.info(
            f"MongoDB. User state updated, state={state}")
    except Exception as e:
        logger.error(f"MongoDB. User state update failed: {e}")
        raise Exception

    return result


async def get_user_state(user_id: 1, collection=user_state) -> bool:
    try:
        current_user_state = await collection.find_one({"user_id": user_id})
        if current_user_state:
            logger.info(f"MongoDB. Current user state: {current_user_state["is_active"]}")

            return current_user_state["is_active"]
    except Exception as e:
        logger.error(f"MongoDB. Phrases can't be updated: {e}")
        raise Exception

    return False


# Was used to fill MongoDB with phrases
# async def insert_phrases(collection=phrases) -> InsertManyResult:
#     payload = [{"phrase_id": int(phrase_id), "phrase": phrase} for phrase_id, phrase in phrases_to_db.items()]
#     try:
#         inserted_data = await collection.insert_many(payload)
#         logger.info(f"MongoDB. Inserted {len(inserted_data.inserted_ids)} phrases into the 'Phrase' collection.")
#     except Exception as e:
#         logger.error(f"MongoDB. Phrases can't be updated: {e}")
#         raise Exception
#
#     return inserted_data


async def get_phrase(phrase_id: int, collection=phrases) -> str:
    try:
        fetched_phrase = await collection.find_one({"phrase_id": phrase_id})
        if fetched_phrase:
            return fetched_phrase["phrase"]
    except Exception as e:
        logger.error(f"MongoDB. Phrases can't be fetched: {e}")
        raise Exception

    return "Failed to fetch phrase from DB. Please, connect to administrator"
