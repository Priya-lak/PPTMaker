from typing import Optional

from libs.PPTMaker.platform.modules.bot.src.utils.styles.base_style import (
    BasePresentationStyle,
    PresentationStyleConfig,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.classy_style import ClassyStyle
from libs.PPTMaker.platform.modules.bot.src.utils.styles.corporate_style import (
    CorporateStyle,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.creative_style import (
    CreativeStyle,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.dark_style import DarkStyle
from libs.PPTMaker.platform.modules.bot.src.utils.styles.minimalist_style import (
    MinimalistStyle,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.professional_style import (
    ProfessionalStyle,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.punk_style import PunkStyle
from libs.PPTMaker.platform.modules.bot.src.utils.styles.style_constants import (
    StyleTheme,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles.vibrant_style import (
    VibrantStyle,
)


class StyleFactory:
    """Factory class to create presentation styles"""

    _styles = {
        StyleTheme.PROFESSIONAL: ProfessionalStyle,
        StyleTheme.MINIMALIST: MinimalistStyle,
        StyleTheme.PUNK: PunkStyle,
        StyleTheme.CLASSY: ClassyStyle,
        StyleTheme.DARK: DarkStyle,
        StyleTheme.VIBRANT: VibrantStyle,
    }

    @classmethod
    def create_style(
        cls, theme: StyleTheme, config: Optional[PresentationStyleConfig] = None
    ) -> BasePresentationStyle:
        """Create a presentation style instance"""
        if theme not in cls._styles:
            raise ValueError(f"Unknown style theme: {theme}")

        style_class = cls._styles[theme]
        return style_class(config)

    @classmethod
    def get_available_themes(cls) -> list[StyleTheme]:
        """Get list of available style themes"""
        return list(cls._styles.keys())

    @classmethod
    def register_style(cls, theme: StyleTheme, style_class: type):
        """Register a new custom style"""
        cls._styles[theme] = style_class
