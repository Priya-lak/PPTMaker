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


class MinimalistStyle(BasePresentationStyle):
    """Minimalist presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.MINIMALIST,
            title="Minimalist",
            description="Clean, simple design with minimal colors",
            font_family_primary="Helvetica",
            font_family_secondary="Arial",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.GRAY_DARK.value,
            primary_medium=ColorEnum.GRAY_MEDIUM.value,
            primary_light=ColorEnum.GRAY_LIGHT.value,
            accent=ColorEnum.CLEAN_BLUE.value,
            text_primary=ColorEnum.GRAY_DARK.value,
            text_secondary=ColorEnum.GRAY_MEDIUM.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.BACKGROUND_LIGHT.value,
            success=ColorEnum.GREEN_SUCCESS.value,
            warning=ColorEnum.YELLOW_WARNING.value,
            danger=ColorEnum.RED.value,
        )

    def _create_dimensions(self) -> Dict[str, Any]:
        # Minimalist style uses more white space
        dims = super()._create_dimensions()
        dims.update(
            {
                "margin_standard": Inches(1),
                "margin_large": Inches(1.5),
                "spacing_medium": Inches(0.75),
                "spacing_large": Inches(1.5),
            }
        )
        return dims


# def main():
#     prs = Presentation()
#     style = MinimalistStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Minimalist Design"
#     subtitle_text = "Less is more. A clean, purposeful look."
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/minimalist-style.pptx")


# if __name__ == "__main__":
#     main()
