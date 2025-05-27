import json
import traceback

from libs.PPTMaker.enums.themes_styles_enum import StylesEnum
from libs.PPTMaker.platform.modules.bot.src.constants import (
    CONTENT_GENERATION_PROMPT,
    CUSTOMIZE_CONTENT_PROMPT,
)
from libs.PPTMaker.platform.modules.bot.src.models.custom_content_models import (
    ContentCustomizationParams,
)
from libs.PPTMaker.platform.modules.bot.src.models.slide_layout_models import (
    PresentationModel,
)
from libs.PPTMaker.platform.modules.bot.src.services.image_search_service import (
    ImageSearchService,
)
from libs.PPTMaker.platform.modules.bot.src.services.llm_service import LLMService
from libs.PPTMaker.platform.modules.bot.src.services.ppt_maker_service import (
    PPTXGenerator,
)
from libs.PPTMaker.platform.modules.bot.src.utils.prompt_formatter_util import (
    params_to_prompt_string,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles import StyleFactory
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("PPTGeneratorService", is_request=False)

logger, listener = log.get_logger()

listener.start()


class PPTGenerator:
    def __init__(self, style: StylesEnum, theme: str = None):
        self.llm_service = LLMService()
        self.style = StyleFactory.create_style(style)
        self.ppt_service = PPTXGenerator(style=self.style, theme=theme)
        self.image_search_service = ImageSearchService()

    def generate_content(self, topic: str, custom_params: ContentCustomizationParams):
        formatted_custom_params = params_to_prompt_string(custom_params)
        logger.info(f"custom params {formatted_custom_params}")
        messages = [
            {"role": "system", "content": CONTENT_GENERATION_PROMPT},
            {
                "role": "system",
                "content": CUSTOMIZE_CONTENT_PROMPT.format(
                    parameters=formatted_custom_params
                ),
            },
            {
                "role": "user",
                "content": f"create presentation points on the topic: {topic}",
            },
        ]
        logger.info("Calling LLM")
        response = self.llm_service.call_llm(
            messages, response_format={"type": "json_object"}
        )
        response = PresentationModel(**json.loads(response))

        return response

    def _save_presentation(self, title):
        try:
            logger.info("Saving presentation to file")
            output_file = f"temp/{title}.pptx".replace(" ", "-")
            self.ppt_service.save_presentation(output_file)
            logger.info(f"Presentation saved to {output_file}")
            return output_file
        except Exception as e:
            logger.error(f"An error occurred while saving presentation {str(e)}")
            raise e

    def create_presentation_from_content(self, content: PresentationModel) -> str:
        logger.info("Creating presentation from content")
        try:
            title = content.title
            for content_slides in content.presentation_content:
                logger.info(f"Content: {content_slides}")
                self.ppt_service.layout_manager.create_slide(
                    **content_slides.model_dump()
                )
            output_file = self._save_presentation(title=title)
            return output_file
        except Exception as e:
            logger.error(
                f"An error occurred while creating presentation {traceback.print_exc()}"
            )
            return None


def main():
    style = StylesEnum.DARK
    topic = "Music genres"
    service = PPTGenerator(
        style=style.value, theme="static/templates/blue-spheres.pptx"
    )
    content = service.generate_content(topic)
    service.create_presentation_from_content(content=content)


if __name__ == "__main__":
    main()
