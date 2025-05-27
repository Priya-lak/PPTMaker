from enum import Enum


class ThemesEnum(Enum):
    MADISON = "static/templates/madison.pptx"
    ION = "static/templates/ion-boardroom.pptx"


class StylesEnum(str, Enum):
    """Available presentation style themes"""

    PROFESSIONAL = "professional"
    MINIMALIST = "minimalist"
    PUNK = "punk"
    CLASSY = "classy"
    CORPORATE = "corporate"
    CREATIVE = "creative"
    DARK = "dark"
    VIBRANT = "vibrant"
