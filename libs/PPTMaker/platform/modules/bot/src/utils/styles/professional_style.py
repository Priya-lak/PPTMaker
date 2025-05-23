from typing import Any, Dict

from pptx import Presentation
from pptx.util import Inches, Pt

from libs.PPTMaker.enums.colors_enum import ColorEnum

# from libs.PPTMaker.platform.modules.bot.src.utils.slides_util import SlideLayoutManager
from libs.PPTMaker.platform.modules.bot.src.utils.styles.base_style import (
    BasePresentationStyle,
    PresentationStyleConfig,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.style_constants import (
    ColorPalette,
    FontStyle,
    StyleTheme,
)


class ProfessionalStyle(BasePresentationStyle):
    """Professional/Corporate presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.PROFESSIONAL,
            title="Professional",
            description="Clean, corporate styling with blue color scheme",
            font_family_primary="Calibri",
            font_family_secondary="Arial",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.BLUE_DARK.value,
            primary_medium=ColorEnum.BLUE_MEDIUM.value,
            primary_light=ColorEnum.BLUE_LIGHT.value,
            accent=ColorEnum.GOLD_DARK.value,
            text_primary=ColorEnum.BLACK.value,
            text_secondary=ColorEnum.GRAY_DARK.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.LIGHT_PINK.value,
            success=ColorEnum.GREEN_SUCCESS.value,
            warning=ColorEnum.YELLOW_WARNING.value,
            danger=ColorEnum.RED.value,
        )


# def main():
#     prs = Presentation()
#     style = ProfessionalStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Professional styling"
#     subtitle_text = "Professional style"
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/professional-style.pptx")


# if __name__ == "__main__":
#     main()
