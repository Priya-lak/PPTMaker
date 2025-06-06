from enum import Enum
from pathlib import Path

TEMPLATE_DIR = "static/templates"


def create_themes_enum():
    """Dynamically create ThemesEnum based on templates in static/templates folder"""

    templates_dir = Path("static/templates")
    custom_paths = {"ion": "ion-boardroom.pptx"}

    # Get all .pptx files in the templates directory
    if templates_dir.exists():
        template_files = [f.name for f in templates_dir.glob("*.pptx")]
    else:
        # Fallback list if directory doesn't exist (for development/testing)
        template_files = [
            "madison.pptx",
            "madison-lilac.pptx",
            "blue-spheres.pptx",
            "bohemian.pptx",
            "canva-portfolio.pptx",
            "designer-template.pptx",
            "dividend-navy.pptx",
            "gradient-pink.pptx",
            "holographic.pptx",
            "ion-boardroom.pptx",
            "mesh-black.pptx",
            "nature.pptx",
            "sales-blue.pptx",
            "slide-blue.pptx",
        ]

    # Create enum members dictionary
    enum_members = {}

    for template_file in sorted(template_files):
        # Extract theme name from filename
        theme_name = template_file.replace(".pptx", "")

        # Handle custom mappings (reverse lookup)
        enum_value = theme_name
        for key, value in custom_paths.items():
            if value == template_file:
                enum_value = key
                break

        # Convert to uppercase for enum constant name
        enum_constant = enum_value.upper().replace("-", "_")
        enum_members[enum_constant] = enum_value

    # Create the enum class dynamically
    ThemesEnum = Enum("ThemesEnum", enum_members, type=str)

    # Add custom methods to the enum
    def template_path(self):
        """Get the full path to the template file"""
        custom_paths_local = {"ion": "ion-boardroom.pptx"}
        filename = custom_paths_local.get(self.value, f"{self.value}.pptx")
        return f"static/templates/{filename}"

    def get_available_themes(cls):
        """Get a list of all available theme names"""
        return [member.value for member in cls]

    def refresh_themes():
        """Refresh and return a new ThemesEnum with current templates"""
        return create_themes_enum()

    # Attach methods to the enum
    ThemesEnum.template_path = property(template_path)
    ThemesEnum.get_available_themes = classmethod(get_available_themes)
    ThemesEnum.refresh_themes = staticmethod(refresh_themes)

    return ThemesEnum


# Create the enum instance
ThemesEnum = create_themes_enum()


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
