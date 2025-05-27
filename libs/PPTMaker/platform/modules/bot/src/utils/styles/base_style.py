from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

from pptx.util import Inches, Pt
from pydantic import BaseModel, Field

from libs.PPTMaker.enums.themes_styles_enum import StylesEnum
from libs.PPTMaker.platform.modules.bot.src.utils.styles.style_constants import (
    ColorPalette,
    FontStyle,
)


class PresentationStyleConfig(BaseModel):
    """Pydantic model for presentation style configuration"""

    theme: StylesEnum
    title: str = Field(..., description="Display name for the style")
    description: str = Field(..., description="Description of the style")
    font_family_primary: str = Field(
        default="Calibri", description="Primary font family"
    )
    font_family_secondary: str = Field(
        default="Arial", description="Secondary font family"
    )
    use_gradients: bool = Field(
        default=False, description="Whether to use gradient backgrounds"
    )
    border_style: str = Field(
        default="none", description="Border style (none, solid, dashed)"
    )
    animation_level: str = Field(
        default="subtle",
        description="Animation intensity (none, subtle, moderate, high)",
    )

    class Config:
        use_enum_values = True


class BasePresentationStyle(ABC):
    """Abstract base class for presentation styles"""

    def __init__(self, config: Optional[PresentationStyleConfig] = None):
        self.config = config or self._get_default_config()
        self.colors = self._create_color_palette()
        self.fonts = self._create_font_styles()
        self.dimensions = self._create_dimensions()
        self.shapes = self._create_shape_styles()

    @abstractmethod
    def _get_default_config(self) -> PresentationStyleConfig:
        """Get default configuration for this style"""
        pass

    @abstractmethod
    def _create_color_palette(self) -> ColorPalette:
        """Create the color palette for this style"""
        pass

    def _create_font_styles(self) -> Dict[str, FontStyle]:
        """Create font styles - can be overridden by subclasses"""
        return {
            "title_large": FontStyle(
                size=Pt(44),
                bold=True,
                color=self.colors.primary_dark,
                font_family=self.config.font_family_primary,
            ),
            "title_medium": FontStyle(
                size=Pt(32),
                bold=True,
                color=self.colors.primary_dark,
                font_family=self.config.font_family_primary,
            ),
            "title_small": FontStyle(
                size=Pt(28),
                bold=True,
                color=self.colors.primary_dark,
                font_family=self.config.font_family_primary,
            ),
            "subtitle": FontStyle(
                size=Pt(24),
                color=self.colors.primary_medium,
                font_family=self.config.font_family_primary,
            ),
            "body_large": FontStyle(
                size=Pt(18),
                color=self.colors.text_primary,
                font_family=self.config.font_family_secondary,
            ),
            "body_medium": FontStyle(
                size=Pt(16),
                color=self.colors.text_primary,
                font_family=self.config.font_family_secondary,
            ),
            "body_small": FontStyle(
                size=Pt(14),
                color=self.colors.text_secondary,
                font_family=self.config.font_family_secondary,
            ),
            "caption": FontStyle(
                size=Pt(14),
                italic=True,
                color=self.colors.text_secondary,
                font_family=self.config.font_family_secondary,
            ),
            "table_header": FontStyle(
                size=Pt(14),
                bold=True,
                color=self.colors.text_light,
                font_family=self.config.font_family_secondary,
            ),
        }

    def _create_dimensions(self) -> Dict[str, Any]:
        """Create standard dimensions"""
        return {
            "slide_width": Inches(13.33),
            "slide_height": Inches(7.5),
            "margin_standard": Inches(0.5),
            "margin_large": Inches(1),
            "spacing_small": Inches(0.25),
            "spacing_medium": Inches(0.5),
            "spacing_large": Inches(1),
        }

    def _create_shape_styles(self) -> Dict[str, Any]:
        """Create shape styling options"""
        return {
            "table_header_fill": self.colors.primary_medium,
            "chart_colors": [
                self.colors.primary_dark,
                self.colors.primary_medium,
                self.colors.accent,
                self.colors.success,
                self.colors.warning,
            ],
            "border_width": Pt(1) if self.config.border_style != "none" else Pt(0),
        }

    def get_background_color(self) -> Any:
        """Get the default background color for the style"""
        return self.colors.background

    def apply_background(self, slide):
        """Apply the background color to a slide"""
        fill = slide.background.fill
        fill.solid()
        fill.fore_color.rgb = self.get_background_color()

    def apply_font_style(self, paragraph, style_name: str):
        """Apply a predefined font style to a paragraph"""
        if style_name in self.fonts:
            style = self.fonts[style_name]
            paragraph.font.size = style.size
            paragraph.font.bold = style.bold
            paragraph.font.italic = style.italic
            if style.color:
                paragraph.font.color.rgb = style.color
            if style.font_family:
                paragraph.font.name = style.font_family

    def get_color(self, color_name: str) -> Any:
        """Get a color by name"""
        return getattr(self.colors, color_name, self.colors.text_primary)

    def get_dimension(self, dimension_name: str) -> Any:
        """Get a dimension by name"""
        return self.dimensions.get(dimension_name, Inches(1))
