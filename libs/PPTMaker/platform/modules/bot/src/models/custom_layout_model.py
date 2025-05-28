from typing import Optional

from pydantic import BaseModel, Field

from libs.PPTMaker.enums.content_gen_enums import *


class SlideLayoutParams(BaseModel):
    """
    Parameters for customizing presentation slide layout and visual structure
    Layout-focused parameters that affect the visual presentation and formatting
    """

    # Slide Structure
    slide_range: Optional[SlideRangeEnum] = Field(
        default=SlideRangeEnum.RANGE_6_9,
        description="Number of slides to generate",
        alias="range",
    )

    # Visual Layout
    visual_preference: Optional[VisualPreferenceEnum] = Field(
        default=VisualPreferenceEnum.BALANCED,
        description="Visual layout and content balance preference",
    )

    data_focus: Optional[DataFocusEnum] = Field(
        default=DataFocusEnum.MODERATE_STATS,
        description="Emphasis on statistics, charts, and data visualization",
    )

    class Config:
        # Allow field aliases (e.g., 'range' instead of 'slide_range')
        validate_by_name = True

        json_schema_extra = {
            "example": {
                "range": "6-9",
                "visual_preference": "balanced",
                "data_focus": "moderate_stats",
            }
        }
