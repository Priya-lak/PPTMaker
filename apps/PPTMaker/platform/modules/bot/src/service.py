from apps.PPTMaker.platform.modules.bot.src.dto import PresentationGenerationRequest
from libs.PPTMaker.enums.themes_styles_enum import StylesEnum
from libs.PPTMaker.platform.modules.bot.src.services.ppt_generator_service import (
    PPTGenerator,
)


def create_customized_presentation(request_data: PresentationGenerationRequest):
    ppt_gen_service = PPTGenerator(style=StylesEnum.CLASSY)
