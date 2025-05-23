import json
import traceback

from libs.PPTMaker.platform.modules.bot.src.constants import CONTENT_GENERATION_PROMPT
from libs.PPTMaker.platform.modules.bot.src.models.content_models import (
    ContentPage,
    ImagePage,
    PresentationModel,
)
from libs.PPTMaker.platform.modules.bot.src.services.llm_service import LLMService
from libs.PPTMaker.platform.modules.bot.src.services.ppt_maker_service import (
    PPTXGenerator,
)
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("GroqLLMService", is_request=False)

logger, listener = log.get_logger()

listener.start()


class PPTGenerator:
    def __init__(self):
        self.llm_service = LLMService()
        self.ppt_service = PPTXGenerator()

    def generate_content(self, topic: str):
        messages = [
            {
                "role": "user",
                "content": f"create presentation points on the topic: {topic}",
            },
            {"role": "system", "content": CONTENT_GENERATION_PROMPT},
        ]
        logger.info("Calling LLM")
        response = self.llm_service.call_llm(
            messages, response_format={"type": "json_object"}
        )
        response = PresentationModel(**json.loads(response))
        logger.info(f"Generated content {response}")

        return response

    def create_presentation_from_content(self, content: PresentationModel):
        logger.info("Creating presentation from content")
        try:
            title = content.title_page.title
            title_slide = self.ppt_service.create_title_slide(
                title, content.title_page.description
            )
            logger.info(f"Title slide {title_slide}")
            for content_slides in content.presentation_content:
                if isinstance(content_slides, ContentPage):
                    slide = self.ppt_service.create_content_slide(
                        content_slides.title, content_slides.bullet_points
                    )
                    logger.info(f"content slide {slide}")

                elif isinstance(content_slides, ImagePage):
                    sample_image_path = "static/images/sample_image.jpg"
                    slide = self.ppt_service.add_image_slide(
                        content_slides.title,
                        sample_image_path,
                        caption=content_slides.caption,
                        layout_type="side_by_side",
                    )
                    logger.info("Image Slide")

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
    service = PPTGenerator()
    content = service.generate_content("GenZ humor")
    service.create_presentation_from_content(content=content)


if __name__ == "__main__":
    main()
