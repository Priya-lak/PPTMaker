from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional

from pptx.dml.color import RGBColor


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
