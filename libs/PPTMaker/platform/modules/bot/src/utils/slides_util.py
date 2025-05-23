from pptx.enum.text import PP_ALIGN
from pptx.util import Inches


class SlideLayoutManager:
    """Handles slide layout creation and management"""

    def __init__(self, presentation, style):
        self.prs = presentation
        self.style = style

    def create_title_slide(self, title, subtitle=""):
        """Create a title slide with title and subtitle"""
        title_slide_layout = self.prs.slide_layouts[0]
        slide = self.prs.slides.add_slide(title_slide_layout)

        # Set and format title
        title_placeholder = slide.shapes.title
        title_placeholder.text = title
        title_paragraph = title_placeholder.text_frame.paragraphs[0]
        self.style.apply_font_style(title_paragraph, "title_large")

        # Set and format subtitle if provided
        if subtitle:
            subtitle_placeholder = slide.placeholders[1]
            subtitle_placeholder.text = subtitle
            subtitle_paragraph = subtitle_placeholder.text_frame.paragraphs[0]
            self.style.apply_font_style(subtitle_paragraph, "subtitle")

        return slide

    def create_content_slide(self, title, bullet_points):
        """Create a slide with title and bullet points"""
        bullet_slide_layout = self.prs.slide_layouts[1]
        slide = self.prs.slides.add_slide(bullet_slide_layout)

        # Set and format title
        title_shape = slide.shapes.title
        title_shape.text = title
        title_paragraph = title_shape.text_frame.paragraphs[0]
        self.style.apply_font_style(title_paragraph, "title_medium")

        # Add and format bullet points
        content_shape = slide.placeholders[1]
        text_frame = content_shape.text_frame
        text_frame.clear()

        for i, point in enumerate(bullet_points):
            if i == 0:
                p = text_frame.paragraphs[0]
            else:
                p = text_frame.add_paragraph()

            p.text = point
            p.level = 0
            self.style.apply_font_style(p, "body_large")

        return slide

    def create_blank_slide_with_title(self, title):
        """Create a blank slide with a centered title"""
        blank_slide_layout = self.prs.slide_layouts[6]
        slide = self.prs.slides.add_slide(blank_slide_layout)

        # Add title
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

        return slide
