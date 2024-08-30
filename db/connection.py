from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import Config, load_config

config: Config = load_config()

uri = config.db.database_url

client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

db = client['good-morning-bot']
user_data = db['user_data']
phrases = db['phrases']
