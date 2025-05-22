import json
from typing import List, Dict, Any, Tuple, Optional
import uuid
from pptx import Presentation

from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("GroqLLMService", is_request=False)

logger, listener = log.get_logger()

listener.start()
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE
import os


class PPTXGenerator:
    def __init__(self):
        """Initialize a new presentation"""
        self.prs = Presentation()
        # Set slide dimensions (16:9 aspect ratio)
        self.prs.slide_width = Inches(13.33)
        self.prs.slide_height = Inches(7.5)

    def create_title_slide(self, title, subtitle=""):
        """Create a title slide with title and subtitle"""
        # Use title slide layout (layout index 0)
        title_slide_layout = self.prs.slide_layouts[0]
        slide = self.prs.slides.add_slide(title_slide_layout)

        # Set title
        title_placeholder = slide.shapes.title
        title_placeholder.text = title

        # Format title
        title_paragraph = title_placeholder.text_frame.paragraphs[0]
        title_paragraph.font.size = Pt(44)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 73, 125)  # Dark blue

        # Set subtitle if provided
        if subtitle:
            subtitle_placeholder = slide.placeholders[1]
            subtitle_placeholder.text = subtitle

            # Format subtitle
            subtitle_paragraph = subtitle_placeholder.text_frame.paragraphs[0]
            subtitle_paragraph.font.size = Pt(24)
            subtitle_paragraph.font.color.rgb = RGBColor(68, 114, 196)  # Medium blue

        return slide

    def create_content_slide(self, title, bullet_points):
        """Create a slide with title and bullet points"""
        # Use content slide layout (layout index 1)
        bullet_slide_layout = self.prs.slide_layouts[1]
        slide = self.prs.slides.add_slide(bullet_slide_layout)

        # Set title
        title_shape = slide.shapes.title
        title_shape.text = title

        # Format title
        title_paragraph = title_shape.text_frame.paragraphs[0]
        title_paragraph.font.size = Pt(32)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 73, 125)

        # Add bullet points
        content_shape = slide.placeholders[1]
        text_frame = content_shape.text_frame
        text_frame.clear()  # Clear existing text

        for i, point in enumerate(bullet_points):
            if i == 0:
                # Use existing paragraph for first bullet
                p = text_frame.paragraphs[0]
            else:
                # Add new paragraph for additional bullets
                p = text_frame.add_paragraph()

            p.text = point
            p.level = 0  # Main bullet level
            p.font.size = Pt(18)
            p.font.color.rgb = RGBColor(0, 0, 0)  # Black text

        return slide

    def add_image_slide(self, title, image_path, caption=""):
        """Create a slide with title, image, and optional caption"""
        # Use blank slide layout
        blank_slide_layout = self.prs.slide_layouts[6]
        slide = self.prs.slides.add_slide(blank_slide_layout)

        # Add title
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(12.33), Inches(1)
        )
        title_frame = title_box.text_frame
        title_frame.text = title
        title_paragraph = title_frame.paragraphs[0]
        title_paragraph.font.size = Pt(32)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 73, 125)
        title_paragraph.alignment = PP_ALIGN.CENTER

        # Add image (check if file exists)
        if os.path.exists(image_path):
            # Calculate image position and size
            img_left = Inches(2)
            img_top = Inches(2)
            img_width = Inches(9.33)
            img_height = Inches(4)

            pic = slide.shapes.add_picture(
                image_path, img_left, img_top, img_width, img_height
            )

            # Add caption if provided
            if caption:
                caption_box = slide.shapes.add_textbox(
                    Inches(2), Inches(6.5), Inches(9.33), Inches(0.5)
                )
                caption_frame = caption_box.text_frame
                caption_frame.text = caption
                caption_paragraph = caption_frame.paragraphs[0]
                caption_paragraph.font.size = Pt(14)
                caption_paragraph.font.italic = True
                caption_paragraph.alignment = PP_ALIGN.CENTER
        else:
            # Add placeholder text if image not found
            placeholder_box = slide.shapes.add_textbox(
                Inches(2), Inches(3), Inches(9.33), Inches(2)
            )
            placeholder_frame = placeholder_box.text_frame
            placeholder_frame.text = f"Image not found: {image_path}"
            placeholder_paragraph = placeholder_frame.paragraphs[0]
            placeholder_paragraph.font.size = Pt(18)
            placeholder_paragraph.alignment = PP_ALIGN.CENTER

        return slide

    def add_chart_slide(self, title, chart_data, chart_type="column"):
        """Create a slide with a chart"""
        # Use blank slide layout
        blank_slide_layout = self.prs.slide_layouts[6]
        slide = self.prs.slides.add_slide(blank_slide_layout)

        # Add title
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(12.33), Inches(1)
        )
        title_frame = title_box.text_frame
        title_frame.text = title
        title_paragraph = title_frame.paragraphs[0]
        title_paragraph.font.size = Pt(28)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 73, 125)
        title_paragraph.alignment = PP_ALIGN.CENTER

        # Create chart data
        chart_data_obj = CategoryChartData()

        # Add categories (x-axis labels)
        categories = list(chart_data.keys())
        chart_data_obj.categories = categories

        # Add series data (assuming single series for simplicity)
        values = list(chart_data.values())
        chart_data_obj.add_series("Series 1", values)

        # Add chart to slide
        x, y, cx, cy = Inches(1.5), Inches(2), Inches(10), Inches(4.5)

        if chart_type.lower() == "column":
            chart_type_enum = XL_CHART_TYPE.COLUMN_CLUSTERED
        elif chart_type.lower() == "pie":
            chart_type_enum = XL_CHART_TYPE.PIE
        elif chart_type.lower() == "line":
            chart_type_enum = XL_CHART_TYPE.LINE
        else:
            chart_type_enum = XL_CHART_TYPE.COLUMN_CLUSTERED

        graphic_frame = slide.shapes.add_chart(
            chart_type_enum, x, y, cx, cy, chart_data_obj
        )
        chart = graphic_frame.chart

        # Customize chart appearance
        chart.has_legend = True
        chart.legend.position = 2  # Right side

        return slide

    def add_text_box(self, slide, text, left, top, width, height, font_size=18):
        """Add a text box to a slide"""
        text_box = slide.shapes.add_textbox(
            Inches(left), Inches(top), Inches(width), Inches(height)
        )
        text_frame = text_box.text_frame
        text_frame.text = text

        # Format text
        paragraph = text_frame.paragraphs[0]
        paragraph.font.size = Pt(font_size)
        paragraph.font.color.rgb = RGBColor(0, 0, 0)

        return text_box

    def add_shape(self, slide, shape_type, left, top, width, height, fill_color=None):
        """Add a shape to a slide"""
        if shape_type.lower() == "rectangle":
            shape = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(left),
                Inches(top),
                Inches(width),
                Inches(height),
            )
        elif shape_type.lower() == "circle":
            shape = slide.shapes.add_shape(
                MSO_SHAPE.OVAL, Inches(left), Inches(top), Inches(width), Inches(height)
            )
        else:
            shape = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                Inches(left),
                Inches(top),
                Inches(width),
                Inches(height),
            )

        # Set fill color if provided
        if fill_color:
            fill = shape.fill
            fill.solid()
            if isinstance(fill_color, tuple) and len(fill_color) == 3:
                fill.fore_color.rgb = RGBColor(*fill_color)

        return shape

    def create_table_slide(self, title, table_data):
        """Create a slide with a table"""
        blank_slide_layout = self.prs.slide_layouts[6]
        slide = self.prs.slides.add_slide(blank_slide_layout)

        # Add title
        title_box = slide.shapes.add_textbox(
            Inches(0.5), Inches(0.5), Inches(12.33), Inches(1)
        )
        title_frame = title_box.text_frame
        title_frame.text = title
        title_paragraph = title_frame.paragraphs[0]
        title_paragraph.font.size = Pt(28)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 73, 125)
        title_paragraph.alignment = PP_ALIGN.CENTER

        # Create table
        rows = len(table_data)
        cols = len(table_data[0]) if table_data else 0

        if rows > 0 and cols > 0:
            left = Inches(1)
            top = Inches(2)
            width = Inches(11.33)
            height = Inches(4.5)

            table = slide.shapes.add_table(rows, cols, left, top, width, height).table

            # Populate table
            for row_idx, row_data in enumerate(table_data):
                for col_idx, cell_data in enumerate(row_data):
                    cell = table.cell(row_idx, col_idx)
                    cell.text = str(cell_data)

                    # Format header row
                    if row_idx == 0:
                        cell.fill.solid()
                        cell.fill.fore_color.rgb = RGBColor(68, 114, 196)
                        cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(
                            255, 255, 255
                        )
                        cell.text_frame.paragraphs[0].font.bold = True

        return slide

    def save_presentation(self, filename):
        """Save the presentation to a file"""
        try:
            self.prs.save(filename)
            print(f"Presentation saved as: {filename}")
            return True
        except Exception as e:
            print(f"Error saving presentation: {e}")
            return False


# Example usage and demonstration
def create_sample_presentation():
    """Create a sample presentation demonstrating all features"""

    # Initialize generator
    ppt_gen = PPTXGenerator()

    # 1. Create title slide
    ppt_gen.create_title_slide(
        title="Python-PPTX Demo Presentation",
        subtitle="Demonstrating Basic PowerPoint Operations",
    )

    # 2. Create content slide with bullet points
    bullet_points = [
        "Create professional presentations programmatically",
        "Add various types of content (text, images, charts)",
        "Customize formatting and styling",
        "Automate repetitive presentation tasks",
        "Export to standard PowerPoint formats",
    ]
    ppt_gen.create_content_slide("Key Features", bullet_points)

    # 3. Create image slide (note: you'll need to provide an actual image path)
    # ppt_gen.add_image_slide(
    #     title="Sample Image Slide",
    #     image_path="sample_image.jpg",  # Replace with actual image path
    #     caption="This is a sample image caption"
    # )

    # 4. Create chart slide
    chart_data = {"Q1": 20, "Q2": 35, "Q3": 42, "Q4": 28}
    ppt_gen.add_chart_slide("Quarterly Results", chart_data, "column")

    # 5. Create table slide
    table_data = [
        ["Product", "Q1 Sales", "Q2 Sales", "Q3 Sales"],
        ["Product A", "$10,000", "$12,000", "$15,000"],
        ["Product B", "$8,000", "$9,500", "$11,000"],
        ["Product C", "$15,000", "$18,000", "$20,000"],
    ]
    ppt_gen.create_table_slide("Sales Data", table_data)

    # 6. Create a custom slide with shapes and text boxes
    blank_slide_layout = ppt_gen.prs.slide_layouts[6]
    custom_slide = ppt_gen.prs.slides.add_slide(blank_slide_layout)

    # Add custom title
    ppt_gen.add_text_box(custom_slide, "Custom Slide with Shapes", 1, 0.5, 11.33, 1, 28)

    # Add shapes
    ppt_gen.add_shape(custom_slide, "rectangle", 2, 2, 3, 1.5, (68, 114, 196))
    ppt_gen.add_shape(custom_slide, "circle", 8, 2, 2, 2, (255, 192, 0))

    # Add text over shapes
    ppt_gen.add_text_box(custom_slide, "Rectangle", 2.5, 2.5, 2, 0.5, 16)
    ppt_gen.add_text_box(custom_slide, "Circle", 8.5, 2.8, 1, 0.5, 16)

    # Save the presentation
    ppt_gen.save_presentation("sample_presentation.pptx")

    return ppt_gen


def create_quick_presentation(title, slides_data, filename):
    """Quickly create a presentation from structured data"""
    ppt_gen = PPTXGenerator()

    # Create title slide
    ppt_gen.create_title_slide(title)

    # Create content slides
    for slide_info in slides_data:
        if slide_info["type"] == "content":
            ppt_gen.create_content_slide(slide_info["title"], slide_info["content"])
        elif slide_info["type"] == "chart":
            ppt_gen.add_chart_slide(
                slide_info["title"],
                slide_info["data"],
                slide_info.get("chart_type", "column"),
            )
        elif slide_info["type"] == "table":
            ppt_gen.create_table_slide(slide_info["title"], slide_info["data"])

    # Save presentation
    ppt_gen.save_presentation(filename)
    return ppt_gen


# Example of quick presentation creation
if __name__ == "__main__":
    # Create sample presentation
    create_sample_presentation()

    # Example of quick presentation creation
    quick_slides = [
        {
            "type": "content",
            "title": "Project Overview",
            "content": [
                "Goal: Automate presentation creation",
                "Timeline: 4 weeks",
                "Team: 3 developers",
            ],
        },
        {
            "type": "chart",
            "title": "Progress Tracking",
            "data": {"Week 1": 25, "Week 2": 50, "Week 3": 75, "Week 4": 100},
            "chart_type": "line",
        },
    ]

    create_quick_presentation(
        "Project Status Update", quick_slides, "quick_presentation.pptx"
    )
