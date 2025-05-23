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


class PunkStyle(BasePresentationStyle):
    """Punk style with edgy, neon-urban aesthetics"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.PUNK,
            title="Punk",
            description="Urban, rebellious look with neon-inspired accents and heavy contrast",
            font_family_primary="Impact",
            font_family_secondary="Arial Black",
            border_style="solid",
            animation_level="high",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.BLACK.value,
            primary_medium=ColorEnum.RED.value,
            primary_light=ColorEnum.HOT_PINK.value,
            accent=ColorEnum.YELLOW.value,
            text_primary=ColorEnum.WHITE.value,
            text_secondary=ColorEnum.GRAY_LIGHT.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.BACKGROUND_DARK.value,
            success=ColorEnum.GREEN_BRIGHT.value,
            warning=ColorEnum.ORANGE.value,
            danger=ColorEnum.RED.value,
        )

    def _create_font_styles(self) -> Dict[str, FontStyle]:
        fonts = super()._create_font_styles()

        # Reinforce punk theme with aggressive, bold fonts
        for key in ["title_large", "title_medium", "title_small", "subtitle"]:
            fonts[key].bold = True
            fonts[key].color = self.colors.accent  # Use neon yellow for impact

        fonts["body_large"].color = self.colors.text_primary
        fonts["body_medium"].color = self.colors.text_primary

        fonts["caption"].italic = True
        fonts["caption"].color = self.colors.primary_light  # Hot pink for flair

        return fonts


# def main():
#     prs = Presentation()
#     style = PunkStyle()
#     layout_manager = SlideLayoutManager(prs, style)
#     title_text = "Punk Design"
#     subtitle_text = "Punk design"
#     layout_manager.create_title_slide(title=title_text, subtitle=subtitle_text)
#     prs.save("output/demo/punk-style.pptx")


# if __name__ == "__main__":
#     main()
