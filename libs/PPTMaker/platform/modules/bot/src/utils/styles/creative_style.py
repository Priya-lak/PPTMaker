from typing import Any, Dict

from pptx.util import Inches, Pt

from libs.PPTMaker.enums.colors_enum import ColorEnum
from libs.PPTMaker.platform.modules.bot.src.config.style_config import (
    ColorPalette,
    FontStyle,
    PresentationStyleConfig,
    StyleTheme,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.base_style import (
    BasePresentationStyle,
)


class CreativeStyle(BasePresentationStyle):
    """Creative/Artistic presentation style with vibrant and playful design elements"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.CREATIVE,
            title="Creative",
            description="Artistic design with bold colors and creative typography",
            font_family_primary="Comic Sans MS",
            font_family_secondary="Trebuchet MS",
            use_gradients=True,
            border_style="dashed",
            animation_level="high",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.DARK_PURPLE.value,
            primary_medium=ColorEnum.TOMATO.value,
            primary_light=ColorEnum.LIGHT_PINK.value,
            accent=ColorEnum.GOLD.value,
            text_primary=ColorEnum.INDIGO.value,
            text_secondary=ColorEnum.PURPLE.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.CORNSILK.value,
            success=ColorEnum.LIME_GREEN.value,
            warning=ColorEnum.ORANGE.value,
            danger=ColorEnum.RED_ORANGE.value,
        )

    def _create_font_styles(self) -> Dict[str, FontStyle]:
        fonts = super()._create_font_styles()

        # Creative style uses more playful font characteristics
        fonts["title_large"] = FontStyle(
            size=Pt(48),
            bold=True,
            color=self.colors.primary_dark,
            font_family="Comic Sans MS",
        )
        fonts["title_medium"] = FontStyle(
            size=Pt(36),
            bold=True,
            color=self.colors.primary_medium,
            font_family="Comic Sans MS",
        )
        fonts["title_small"] = FontStyle(
            size=Pt(30),
            bold=True,
            italic=True,
            color=self.colors.primary_dark,
            font_family="Comic Sans MS",
        )
        fonts["subtitle"] = FontStyle(
            size=Pt(26),
            bold=False,
            italic=True,
            color=self.colors.accent,
            font_family="Trebuchet MS",
        )

        # Add some creative-specific font styles
        fonts["creative_highlight"] = FontStyle(
            size=Pt(20),
            bold=True,
            italic=True,
            color=self.colors.primary_medium,
            font_family="Comic Sans MS",
        )
        fonts["playful_text"] = FontStyle(
            size=Pt(16),
            bold=False,
            color=self.colors.primary_dark,
            font_family="Trebuchet MS",
        )

        return fonts

    def _create_dimensions(self) -> Dict[str, Any]:
        dims = super()._create_dimensions()

        # Creative style uses irregular spacing for artistic effect
        dims.update(
            {
                "margin_creative": Inches(0.75),
                "spacing_irregular": Inches(0.4),
                "spacing_artistic": Inches(1.2),
            }
        )

        return dims
