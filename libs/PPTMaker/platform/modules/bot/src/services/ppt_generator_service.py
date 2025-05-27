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
        messages = [
            {"role": "system", "content": CONTENT_GENERATION_PROMPT},
            {
                "role": "system",
                "content": CUSTOMIZE_CONTENT_PROMPT.format(custom_params),
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

    def create_presentation_from_content(self, content: PresentationModel):
        logger.info("Creating presentation from content")
        try:
            title = content.title
            for content_slides in content.presentation_content:
                logger.info(f"Content: {content_slides}")
                self.ppt_service.layout_manager.create_slide(
                    **content_slides.model_dump()
                )

            output_file = f"output/{title}.pptx".replace(" ", "-")
            self.ppt_service.save_presentation(output_file)
            logger.info(f"Presentation saved to {output_file}")
            return True
        except Exception as e:
            logger.error(
                f"An error occurred while creating presentation {traceback.print_exc()}"
            )
            return None


def main():
    themes = [
        StylesEnum.MINIMALIST,
        StylesEnum.PROFESSIONAL,
        StylesEnum.PUNK,
        StylesEnum.CLASSY,
        StylesEnum.CORPORATE,
        StylesEnum.CREATIVE,
        StylesEnum.DARK,
        StylesEnum.VIBRANT,
    ]

    topics = [
        "What If Social Media Was Invented in the 1800s?",
        "A Day in the Life of Your Smartphone's Battery",
        "Why AI Would Totally Flunk Kindergarten",
        "Superheroes and Their Totally Useless Powers",
        "If Netflix Categories Were Honest",
        "Why Cats Would Be Better CEOs",
        "Could We Survive a Zombie Apocalypse... Using Only IKEA Furniture?",
        "Is Cereal a Soup? A Philosophical Debate",
    ]

    style = StylesEnum.DARK
    topic = "Music genres"
    service = PPTGenerator(
        style=style.value, theme="static/templates/blue-spheres.pptx"
    )
    content = service.generate_content(topic)
    service.create_presentation_from_content(content=content)


if __name__ == "__main__":
    main()
