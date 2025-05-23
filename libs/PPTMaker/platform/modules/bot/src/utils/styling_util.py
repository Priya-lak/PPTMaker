from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt


class PresentationStyle:
    """Centralized styling configuration for presentations"""

    def __init__(self):
        # Color Scheme
        self.colors = {
            "primary_dark": RGBColor(31, 73, 125),  # Dark blue
            "primary_medium": RGBColor(68, 114, 196),  # Medium blue
            "primary_light": RGBColor(155, 194, 230),  # Light blue
            "accent": RGBColor(255, 192, 0),  # Gold/Yellow accent
            "text_primary": RGBColor(0, 0, 0),  # Black
            "text_secondary": RGBColor(89, 89, 89),  # Dark gray
            "text_light": RGBColor(255, 255, 255),  # White
            "background": RGBColor(248, 249, 250),  # Light gray background
            "success": RGBColor(40, 167, 69),  # Green
            "warning": RGBColor(255, 193, 7),  # Yellow
            "danger": RGBColor(220, 53, 69),  # Red
        }

        # Typography
        self.fonts = {
            "title_large": {
                "size": Pt(44),
                "bold": True,
                "color": self.colors["primary_dark"],
            },
            "title_medium": {
                "size": Pt(32),
                "bold": True,
                "color": self.colors["primary_dark"],
            },
            "title_small": {
                "size": Pt(28),
                "bold": True,
                "color": self.colors["primary_dark"],
            },
            "subtitle": {
                "size": Pt(24),
                "bold": False,
                "color": self.colors["primary_medium"],
            },
            "body_large": {
                "size": Pt(18),
                "bold": False,
                "color": self.colors["text_primary"],
            },
            "body_medium": {
                "size": Pt(16),
                "bold": False,
                "color": self.colors["text_primary"],
            },
            "body_small": {
                "size": Pt(14),
                "bold": False,
                "color": self.colors["text_secondary"],
            },
            "caption": {
                "size": Pt(14),
                "bold": False,
                "color": self.colors["text_secondary"],
                "italic": True,
            },
            "table_header": {
                "size": Pt(14),
                "bold": True,
                "color": self.colors["text_light"],
            },
        }

        # Layout dimensions
        self.dimensions = {
            "slide_width": Inches(13.33),
            "slide_height": Inches(7.5),
            "margin_standard": Inches(0.5),
            "margin_large": Inches(1),
            "spacing_small": Inches(0.25),
            "spacing_medium": Inches(0.5),
            "spacing_large": Inches(1),
        }

        # Shape styles
        self.shapes = {
            "table_header_fill": self.colors["primary_medium"],
            "chart_colors": [
                self.colors["primary_dark"],
                self.colors["primary_medium"],
                self.colors["accent"],
                self.colors["success"],
                self.colors["warning"],
            ],
        }

    def apply_font_style(self, paragraph, style_name):
        """Apply a predefined font style to a paragraph"""
        if style_name in self.fonts:
            style = self.fonts[style_name]
            paragraph.font.size = style["size"]
            paragraph.font.bold = style["bold"]
            paragraph.font.color.rgb = style["color"]
            if "italic" in style:
                paragraph.font.italic = style["italic"]

    def get_color(self, color_name):
        """Get a color by name"""
        return self.colors.get(color_name, self.colors["text_primary"])

    def get_dimension(self, dimension_name):
        """Get a dimension by name"""
        return self.dimensions.get(dimension_name, Inches(1))
