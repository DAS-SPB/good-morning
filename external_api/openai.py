import requests
import logging

from config.config import Config, load_config
from lexicon.lexicon import LEXICON_RU
from openai import OpenAI

config: Config = load_config()
logger = logging.getLogger(__name__)
client = OpenAI()

openai_api_key = config.ext_api.openai_api_key

ext_api_url = 'https://api.openai.com/v1/chat/completions'

default_response = LEXICON_RU.get('openai_no_response')


async def chat_with_openai(user_request: str) -> str:
    try:
        response = requests.post(
            url=ext_api_url,
            headers={'Content-Type': 'application/json',
                     'Authorization': f'Bearer {openai_api_key}'},
            json={

                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a chatbot that wishes a GM to a cat lover"
                    },
                    {
                        "role": "user",
                        "content": user_request
                    }
                ]
            }
        )

        logger.debug(f"Openai API. Incoming response. Status code: {response.status_code}. Response: {response.text}")

        data = response.json()
        if response.status_code == 200:
            try:
                return data['choices'][0]['message']['content']
            except (KeyError, IndexError, TypeError) as e:
                logger.error(f"Openai API. Invalid incoming response structure: {e}")
                return default_response

        else:
            return default_response

    except requests.exceptions.RequestException as e:
        logger.error(f"Openai API. Request failed: {e}")

        return default_response
