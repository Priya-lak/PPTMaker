from typing import Dict

from pptx import Presentation

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


class VibrantStyle(BasePresentationStyle):
    """Vibrant/Colorful presentation style"""

    def _get_default_config(self) -> PresentationStyleConfig:
        return PresentationStyleConfig(
            theme=StyleTheme.VIBRANT,
            title="Vibrant",
            description="Energetic design with bright, bold colors",
            font_family_primary="Trebuchet MS",
            font_family_secondary="Verdana",
            use_gradients=True,
            animation_level="moderate",
        )

    def _create_color_palette(self) -> ColorPalette:
        return ColorPalette(
            primary_dark=ColorEnum.BLUE_VIOLET.value,
            primary_medium=ColorEnum.DEEP_PINK.value,
            primary_light=ColorEnum.HOT_PINK.value,
            accent=ColorEnum.GOLD.value,
            text_primary=ColorEnum.INDIGO.value,
            text_secondary=ColorEnum.PURPLE.value,
            text_light=ColorEnum.WHITE.value,
            background=ColorEnum.ALICE_BLUE.value,
            success=ColorEnum.LIME_GREEN.value,
            warning=ColorEnum.ORANGE.value,
            danger=ColorEnum.RED_ORANGE.value,
        )


def demo_styles():
    prs = Presentation()

    # 2. Apply the Professional Style
    style = VibrantStyle()

    # 3. Add a slide with title and content layout
    slide_layout = prs.slide_layouts[1]  # Title and Content
    slide = prs.slides.add_slide(slide_layout)

    # 4. Set the title
    title = slide.shapes.title
    title.text = "Quarterly Report"
    style.apply_font_style(title.text_frame.paragraphs[0], "title")

    # 5. Add bullet points to content box
    content_box = slide.placeholders[1]
    content_box.text = "Highlights:"
    style.apply_font_style(content_box.text_frame.paragraphs[0], "subtitle")

    # Add bullet points
    bullet_points = ["Revenue up by 15%", "User growth: 20%", "Launched 2 new products"]
    for point in bullet_points:
        p = content_box.text_frame.add_paragraph()
        p.text = point
        p.level = 1  # indent
        style.apply_font_style(p, "normal")

    # 6. Save the presentation
    prs.save("styled_presentation.pptx")


if __name__ == "__main__":
    # Example usage
    demo_styles()
