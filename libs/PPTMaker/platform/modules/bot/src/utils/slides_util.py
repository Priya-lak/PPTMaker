from pptx import Presentation
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches

from libs.PPTMaker.platform.modules.bot.src.models.slide_models import SlideLayout
from libs.PPTMaker.platform.modules.bot.src.utils.styles.styling_util import (
    BasePresentationStyle,
)


class SlideLayoutManager:
    """Handles slide layout creation and management"""

    def __init__(self, presentation: Presentation, style: BasePresentationStyle):
        self.prs = presentation
        self.style = style

    def create_title_slide(self, title: str, subtitle: str = ""):
        """Create a title slide with title and subtitle"""
        layout = self.prs.slide_layouts[SlideLayout.TITLE]
        slide = self.prs.slides.add_slide(layout)

        # Set and format title
        title_placeholder = slide.shapes.title
        title_placeholder.text = title
        self.style.apply_font_style(
            title_placeholder.text_frame.paragraphs[0], "title_large"
        )

        # Set and format subtitle if provided
        if subtitle:
            subtitle_placeholder = slide.placeholders[1]
            subtitle_placeholder.text = subtitle
            self.style.apply_font_style(
                subtitle_placeholder.text_frame.paragraphs[0], "subtitle"
            )
        self.style.apply_background(slide)

        return slide

    def create_content_slide(self, title: str, bullet_points: list[str]):
        """Create a slide with title and bullet points"""
        layout = self.prs.slide_layouts[SlideLayout.TITLE_AND_CONTENT]
        slide = self.prs.slides.add_slide(layout)

        # Set and format title
        title_shape = slide.shapes.title
        title_shape.text = title
        self.style.apply_font_style(
            title_shape.text_frame.paragraphs[0], "title_medium"
        )

        # Add and format bullet points
        content_shape = slide.placeholders[1]
        text_frame = content_shape.text_frame
        text_frame.clear()

        for i, point in enumerate(bullet_points):
            p = text_frame.paragraphs[0] if i == 0 else text_frame.add_paragraph()
            p.text = point
            p.level = 0
            self.style.apply_font_style(p, "body_large")

        self.style.apply_background(slide)

        return slide

    def create_blank_slide_with_title(self, title: str):
        """Create a blank slide with a centered title"""
        layout = self.prs.slide_layouts[SlideLayout.BLANK]
        slide = self.prs.slides.add_slide(layout)

        # Add centered title textbox
        title_box = slide.shapes.add_textbox(
            self.style.get_dimension("margin_standard"),
            Inches(0.3),
            Inches(12),
            self.style.get_dimension("spacing_large"),
        )
        title_frame = title_box.text_frame
        title_frame.text = title
        title_paragraph = title_frame.paragraphs[0]
        self.style.apply_font_style(title_paragraph, "title_medium")
        title_paragraph.alignment = PP_ALIGN.CENTER

        self.style.apply_background(slide)

        return slide
