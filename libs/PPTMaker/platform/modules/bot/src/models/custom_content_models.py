from typing import Optional

from pydantic import BaseModel, Field

from libs.PPTMaker.enums.content_gen_enums import *


class ContentGenerationParams(BaseModel):
    """
    Parameters for customizing presentation content generation
    Content-focused parameters that affect the substance and style of the presentation
    """

    # Core Content Parameters
    tone: Optional[ToneEnum] = Field(
        default=ToneEnum.PROFESSIONAL,
        description="Language style and voice for the presentation",
    )

    length: Optional[LengthEnum] = Field(
        default=LengthEnum.MODERATE, description="Depth and detail level of content"
    )

    # Audience and Purpose
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

    # Domain and Context
    industry: Optional[IndustryEnum] = Field(
        default=IndustryEnum.GENERAL,
        description="Industry or domain focus for specialized content",
    )

    regional_focus: Optional[RegionalFocusEnum] = Field(
        default=RegionalFocusEnum.GLOBAL,
        description="Geographic perspective and regional examples",
    )

    time_duration: Optional[TimeDurationEnum] = Field(
        default=TimeDurationEnum.DURATION_30_MIN,
        description="Expected presentation delivery time",
    )

    # Content Customization
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
        json_schema_extra = {
            "example": {
                "tone": "professional",
                "length": "moderate",
                "target_audience": "executives",
                "presentation_purpose": "sales_pitch",
                "detail_level": "moderate_detail",
                "include_examples": "moderate",
                "engagement_level": "interactive",
                "industry": "technology",
                "regional_focus": "global",
                "time_duration": "30_min",
                "include_call_to_action": True,
                "branded_content": True,
            }
        }
