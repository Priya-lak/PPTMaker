from typing import Optional

from pydantic import BaseModel, Field

from libs.PPTMaker.enums.themes_styles_enum import StylesEnum, ThemesEnum
from libs.PPTMaker.platform.modules.bot.src.models.custom_content_models import (
    ContentGenerationParams,
)
from libs.PPTMaker.platform.modules.bot.src.models.custom_layout_model import (
    SlideLayoutParams,
)


class ContentGenerationRequest(BaseModel):
    """
    Complete request model for presentation generation
    """

    topic: str = Field(
        description="The main topic for presentation generation",
        min_length=3,
        max_length=200,
    )

    content_customization: Optional[ContentGenerationParams] = Field(
        default_factory=ContentGenerationParams,
        description="Content customization parameters",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "topic": "Artificial Intelligence in Healthcare",
                "content_customization": {
                    "tone": "professional",
                    "length": "descriptive",
                    "target_audience": "technical_experts",
                    "presentation_purpose": "conference_talk",
                    "detail_level": "deep_dive",
                    "include_examples": "extensive",
                    "engagement_level": "highly_engaging",
                    "industry": "healthcare",
                },
            }
        }


class PresentationGenerationRequest(BaseModel):
    content: str
    layout_customization: Optional[ContentGenerationParams] = Field(
        default_factory=SlideLayoutParams,
        description="Layout customization parameters",
    )
    style: Optional[StylesEnum] = Field(
        default=StylesEnum.CORPORATE,
        description="Style of the presentation",
    )
    theme: Optional[ThemesEnum] = Field(
        default=None,
        description="Theme of the presentation",
    )

    class Config:
        json_schema_extra = {
            "example": {
                "content": "custom",
                "layout_customization": {
                    "slide_range": "3-5",
                    "visual_preference": "balanced",
                },
            }
        }


class DownloadFileRequest(BaseModel):
    filepath: str = None
