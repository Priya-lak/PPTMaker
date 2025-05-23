from typing import Dict

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
            text_secondary=ColorEnum.DARK_GRAY.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.LIGHT_PINK_GRAY.value,
            success=ColorEnum.SUCCESS_GREEN.value,
            warning=ColorEnum.YELLOW_WARNING.value,
            danger=ColorEnum.RED.value,
        )
