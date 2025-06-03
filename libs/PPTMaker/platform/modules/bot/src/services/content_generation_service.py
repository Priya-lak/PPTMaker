# content_generation_service.py
import traceback
from typing import Optional

from libs.PPTMaker.platform.modules.bot.src.constants import (
    CUSTOMIZE_CONTENT_PROMPT,
)
from libs.PPTMaker.platform.modules.bot.src.models.custom_content_models import (
    ContentGenerationParams,
)
from libs.PPTMaker.platform.modules.bot.src.models.slide_layout_models import (
    PresentationModel,
)
from libs.PPTMaker.platform.modules.bot.src.services.llm_service import LLMService
from libs.PPTMaker.platform.modules.bot.src.utils.prompt_formatter_util import (
    params_to_prompt_string,
)
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("ContentGenerationService", is_request=False)
logger, listener = log.get_logger()
listener.start()


class ContentGenerationService:
    """
    Service responsible for generating presentation content using LLM.
    This service is stateless and focuses solely on content creation.
    """

    def __init__(self):
        self.llm_service = LLMService()

    def generate_content(
        self, topic: str, custom_params: Optional[ContentGenerationParams] = None
    ) -> PresentationModel:
        """
        Generate presentation content for a given topic with optional customization.

        Args:
            topic: The presentation topic
            custom_params: Optional customization parameters

        Returns:
            PresentationModel: Generated content structure

        Raises:
            Exception: If content generation fails
        """
        try:
            messages = self._build_messages(topic, custom_params)

            logger.info(f"Generating content for topic: {topic}")
            response_content = self.llm_service.call_llm(messages)
            logger.info(f"Successfully generated content with slides")

            return response_content

        except Exception as e:
            logger.error(f"Content generation failed: {str(e)}")
            logger.error(traceback.format_exc())
            raise e

    def _build_messages(
        self, topic: str, custom_params: Optional[ContentGenerationParams]
    ) -> list:
        """Build the message array for LLM request."""
        messages = []
        logger.info("Building messages")
        if custom_params:
            logger.info("custom_params")
            formatted_params = params_to_prompt_string(custom_params)

            logger.info(f"Using custom parameters: {formatted_params}")
            prompt = CUSTOMIZE_CONTENT_PROMPT.format(parameters=formatted_params)
            logger.info(f"prompt {prompt}")
            messages.append(
                {
                    "role": "system",
                    "content": prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": f"create presentation points on the topic: {topic}",
            }
        )

        return messages


if __name__ == "__main__":
    service = ContentGenerationService()

    custom_params = ContentGenerationParams(tone="professional", length="comprehensive")
    custom_content = service.generate_content("Advanced AI Concepts", custom_params)
