from typing import Dict

from pptx import Presentation
from pptx.util import Pt

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


class CorporateStyle(BasePresentationStyle):
    """Corporate presentation style - more formal than Professional"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.CORPORATE,
            title="Corporate",
            description="Formal corporate styling with navy and gray tones",
            font_family_primary="Times New Roman",
            font_family_secondary="Arial",
            border_style="solid",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.NAVY_BLUE.value,
            primary_medium=ColorEnum.STEEL_BLUE.value,
            primary_light=ColorEnum.LIGHT_STEEL_BLUE.value,
            accent=ColorEnum.DARK_GOLDENROD.value,
            text_primary=ColorEnum.GRAY_DARKER.value,  # Add DARK_SLATE_GRAY if reused
            text_secondary=ColorEnum.GRAY_DIM.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.WHITE_SMOKE.value,
            success=ColorEnum.DARK_GREEN.value,
            warning=ColorEnum.DARK_ORANGE.value,
            danger=ColorEnum.DARK_RED.value,
        )

    def _create_font_styles(self) -> Dict[str, FontStyle]:
        fonts = super()._create_font_styles()
        # Corporate style uses more conservative font sizes
        fonts["title_large"].size = Pt(36)
        fonts["title_medium"].size = Pt(28)
        fonts["subtitle"].size = Pt(20)
        return fonts


# def main():
#     prs = Presentation()
#     style = CorporateStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Corporate Theme"
#     subtitle_text = "Polished. Professional. Consistent."
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/corporate-style.pptx")


# if __name__ == "__main__":
#     main()
