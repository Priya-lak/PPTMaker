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


class ClassyStyle(BasePresentationStyle):
    """Classy/Elegant presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.CLASSY,
            title="Classy",
            description="Elegant design with sophisticated color palette",
            font_family_primary="Georgia",
            font_family_secondary="Times New Roman",
            use_gradients=True,
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.MIDNIGHT_BLUE.value,
            primary_medium=ColorEnum.DARK_SLATE_BLUE.value,
            primary_light=ColorEnum.MEDIUM_SLATE_BLUE.value,
            accent=ColorEnum.GOLDENROD.value,
            text_primary=ColorEnum.MIDNIGHT_BLUE.value,
            text_secondary=ColorEnum.GRAY_DIM.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.GHOST_WHITE.value,
            success=ColorEnum.FOREST_GREEN.value,
            warning=ColorEnum.DARK_ORANGE.value,
            danger=ColorEnum.FIRE_BRICK.value,
        )
