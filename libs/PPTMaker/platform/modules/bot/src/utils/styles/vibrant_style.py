from typing import Any, Dict

from pptx import Presentation
from pptx.util import Inches, Pt

from libs.PPTMaker.enums.colors_enum import ColorEnum
from libs.PPTMaker.enums.themes_styles_enum import StylesEnum

# from libs.PPTMaker.platform.modules.bot.src.utils.slides_util import SlideLayoutManager
from libs.PPTMaker.platform.modules.bot.src.utils.styles.base_style import (
    BasePresentationStyle,
    PresentationStyleConfig,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.style_constants import (
    ColorPalette,
)


class VibrantStyle(BasePresentationStyle):
    """Vibrant/Colorful presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StylesEnum.VIBRANT,
            title="Vibrant",
            description="Energetic design with bright, bold colors",
            font_family_primary="Trebuchet MS",
            font_family_secondary="Verdana",
            use_gradients=True,
            animation_level="moderate",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.BLUE_DARK.value,
            primary_medium=ColorEnum.DEEP_PINK.value,
            primary_light=ColorEnum.HOT_PINK.value,
            accent=ColorEnum.GOLD.value,
            text_primary=ColorEnum.INDIGO.value,
            text_secondary=ColorEnum.PURPLE.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.BLUE_LIGHT.value,
            success=ColorEnum.LIME_GREEN.value,
            warning=ColorEnum.ORANGE.value,
            danger=ColorEnum.RED_ORANGE.value,
        )


# def main():
#     prs = Presentation()
#     style = VibrantStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Vibrant Style"
#     subtitle_text = "Vibrant styling"
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/vibrant-style.pptx")


# if __name__ == "__main__":
#     main()
