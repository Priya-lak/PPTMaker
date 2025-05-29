from enum import Enum


class ThemesEnum(str, Enum):
    MADISON = "madison"
    MADISON_LILAC = "madison-lilac"
    BLUE_SPHERES = "blue-spheres"
    ION = "ion"

    _CUSTOM_PATHS = {"ion": "ion-boardroom.pptx"}

    @property
    def template_path(self):
        _CUSTOM_PATHS = {"ion": "ion-boardroom.pptx"}
        filename = _CUSTOM_PATHS.get(self.value, f"{self.value}.pptx")
        return f"static/templates/{filename}"


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
