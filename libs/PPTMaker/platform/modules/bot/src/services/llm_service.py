from typing import Dict, List

from groq import Groq
from pydantic import BaseModel

from libs.PPTMaker.platform.modules.bot.src.config.groq_config import (
    GROQ_API_KEY,
    MAX_TOKENS,
    MODEL_NAME,
)
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("GroqLLMService", is_request=False)

logger, listener = log.get_logger()
listener.start()


class LLMService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = MODEL_NAME
        self.max_tokens = MAX_TOKENS

    @staticmethod
    def build_user_message(message):
        return {"role": "user", "content": message}

    def call_llm(self, messages: List[Dict[str, str]], response_format=None):
        response = self.client.chat.completions.create(
            messages=messages,
            model=self.model,
            max_tokens=self.max_tokens,
            response_format=response_format,
        )
        response_content = response.choices[0].message.content
        # logger.info(f"LLM response {response_content}")
        return response_content


def main():
    llm_service = LLMService()
    user_input = "Hi! How are you"
    llm_message = LLMService.build_user_message(user_input)
    response = llm_service.call_llm([llm_message])
    print(f"LLM response {response}")


if __name__ == "__main__":
    main()
