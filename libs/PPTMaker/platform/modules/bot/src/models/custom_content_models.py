from enum import Enum
from typing import Literal, Optional

from pydantic import BaseModel, Field

from libs.PPTMaker.enums.content_gen_enums import *


class ContentCustomizationParams(BaseModel):
    """
    Parameters for customizing presentation content generation
    """

    # Core Parameters
    tone: Optional[ToneEnum] = Field(
        default=ToneEnum.PROFESSIONAL,
        description="Language style and voice for the presentation",
    )

    length: Optional[LengthEnum] = Field(
        default=LengthEnum.MODERATE, description="Depth and detail level of content"
    )

    slide_range: Optional[SlideRangeEnum] = Field(
        default=SlideRangeEnum.RANGE_6_9,
        description="Number of slides to generate",
        alias="range",
    )

    # Advanced Parameters
    target_audience: Optional[TargetAudienceEnum] = Field(
        default=TargetAudienceEnum.GENERAL_PUBLIC,
        description="Intended audience for content complexity and examples",
    )

    presentation_purpose: Optional[PresentationPurposeEnum] = Field(
        default=PresentationPurposeEnum.EDUCATIONAL,
        description="Primary goal and structure of the presentation",
    )

    detail_level: Optional[DetailLevelEnum] = Field(
        default=DetailLevelEnum.MODERATE_DETAIL,
        description="Technical depth and complexity level",
    )

    include_examples: Optional[ExamplesEnum] = Field(
        default=ExamplesEnum.MODERATE,
        description="Amount of examples and case studies to include",
    )

    engagement_level: Optional[EngagementLevelEnum] = Field(
        default=EngagementLevelEnum.INFORMATIONAL,
        description="Level of interactive and engaging elements",
    )

    # Extended Parameters
    industry: Optional[IndustryEnum] = Field(
        default=IndustryEnum.GENERAL,
        description="Industry or domain focus for specialized content",
    )

    visual_preference: Optional[VisualPreferenceEnum] = Field(
        default=VisualPreferenceEnum.BALANCED,
        description="Visual layout and content balance preference",
    )

    data_focus: Optional[DataFocusEnum] = Field(
        default=DataFocusEnum.MODERATE_STATS,
        description="Emphasis on statistics, charts, and data visualization",
    )

    regional_focus: Optional[RegionalFocusEnum] = Field(
        default=RegionalFocusEnum.GLOBAL,
        description="Geographic perspective and regional examples",
    )

    time_duration: Optional[TimeDurationEnum] = Field(
        default=TimeDurationEnum.DURATION_30_MIN,
        description="Expected presentation delivery time",
    )

    # Additional Customization Fields
    specific_requirements: Optional[str] = Field(
        default=None,
        description="Any specific requirements or preferences not covered by other parameters",
        max_length=500,
    )

    avoid_topics: Optional[str] = Field(
        default=None,
        description="Topics or themes to avoid in the presentation",
        max_length=200,
    )

    include_call_to_action: Optional[bool] = Field(
        default=False, description="Whether to include call-to-action elements"
    )

    branded_content: Optional[bool] = Field(
        default=False,
        description="Whether content should be suitable for corporate branding",
    )

    class Config:
        # Allow field aliases (e.g., 'range' instead of 'slide_range')
        validate_by_name = True

        # Example for API documentation
        json_schema_extra = {
            "example": {
                "tone": "professional",
                "length": "moderate",
                "range": "6-9",
                "target_audience": "executives",
                "presentation_purpose": "sales_pitch",
                "detail_level": "moderate_detail",
                "include_examples": "moderate",
                "engagement_level": "interactive",
                "industry": "technology",
                "visual_preference": "balanced",
                "data_focus": "moderate_stats",
                "regional_focus": "global",
                "time_duration": "30_min",
                "include_call_to_action": True,
                "branded_content": True,
            }
        }


# Request model that combines topic with customization parameters
