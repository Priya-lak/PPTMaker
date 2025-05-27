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


class DarkStyle(BasePresentationStyle):
    """Dark theme presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StylesEnum.DARK,
            title="Dark",
            description="Modern dark theme with bright accents",
            font_family_primary="Segoe UI",
            font_family_secondary="Arial",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.WHITE.value,
            primary_medium=ColorEnum.GRAY_LIGHTER.value,
            primary_light=ColorEnum.GRAY_MEDIUM.value,  # Add DARK_GRAY_MEDIUM if reused
            accent=ColorEnum.SPRING_GREEN.value,
            text_primary=ColorEnum.WHITE.value,
            text_secondary=ColorEnum.GRAY_TEXT.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.GRAY_EXTRA_DARK.value,
            success=ColorEnum.SPRING_GREEN.value,
            warning=ColorEnum.GOLD.value,
            danger=ColorEnum.RED_ORANGE.value,
        )


# def main():
#     prs = Presentation()
#     style = DarkStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Dark Mode Showcase"
#     subtitle_text = "Sleek. Modern. Focused."
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/dark-style.pptx")


# if __name__ == "__main__":
#     main()
