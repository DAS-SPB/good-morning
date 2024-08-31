import requests
import logging

from config.config import Config, load_config

config: Config = load_config()
logger = logging.getLogger(__name__)

cat_api_key = config.ext_api.cat_api_key
ext_api_url = 'https://api.thecatapi.com/v1/images/search'

default_gif_file_id = 'BQACAgIAAxkBAAPiZtOBIvDwRO2vTu8dn_LsgbXuVhQAAu1UAAJeZqBKzg3Z_CzRRuQ1BA'


async def get_cat_image() -> str:
    try:
        response = requests.get(ext_api_url, headers={'x-api-key': cat_api_key})

        logger.debug(f"Cat API. Incoming response. Status code: {response.status_code}. Response: {response.text}")

        data = response.json()[0]
        if response.status_code == 200 and 'url' in data:
            return data.get('url')
        else:
            logger.error("Cat API. Incoming response. URL not found in the response.")

            return default_gif_file_id
    except requests.exceptions.RequestException as e:
        logger.error(f"Cat API. Request failed: {e}")

        return default_gif_file_id
