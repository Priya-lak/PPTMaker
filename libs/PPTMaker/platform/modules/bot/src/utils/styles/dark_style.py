from libs.PPTMaker.enums.colors_enum import ColorEnum
from libs.PPTMaker.platform.modules.bot.src.config.style_config import (
    ColorPalette,
    PresentationStyleConfig,
    StyleTheme,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.base_style import (
    BasePresentationStyle,
)


class DarkStyle(BasePresentationStyle):
    """Dark theme presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.DARK,
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
