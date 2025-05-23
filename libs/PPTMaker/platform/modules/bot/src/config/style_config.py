from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional

from pptx.dml.color import RGBColor
from pydantic import BaseModel, Field


class StyleTheme(str, Enum):
    """Available presentation style themes"""

    PROFESSIONAL = "professional"
    MINIMALIST = "minimalist"
    PUNK = "punk"
    CLASSY = "classy"
    CORPORATE = "corporate"
    CREATIVE = "creative"
    DARK = "dark"
    VIBRANT = "vibrant"


class PresentationStyleConfig(BaseModel):
    """Pydantic model for presentation style configuration"""

    theme: StyleTheme
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


@dataclass
class FontStyle:
    """Font styling configuration"""

    size: Any  # Pt object
    bold: bool = False
    italic: bool = False
    color: Any = None  # RGBColor object
    font_family: Optional[str] = None


@dataclass
class ColorPalette:
    """Color palette for a presentation theme"""

    primary_dark: Any
    primary_medium: Any
    primary_light: Any
    accent: Any
    text_primary: Any
    text_secondary: Any
    text_light: Any
    background: Any
    success: Any
    warning: Any
    danger: Any

    def __post_init__(self):
        """Ensure all colors are RGBColor objects"""
        for field_name, value in self.__dict__.items():
            if isinstance(value, tuple) and len(value) == 3:
                setattr(self, field_name, RGBColor(*value))
