from typing import Optional

from pydantic import BaseModel, Field

from libs.PPTMaker.platform.modules.bot.src.models.custom_content_models import (
    ContentCustomizationParams,
)


class PresentationGenerationRequest(BaseModel):
    """
    Complete request model for presentation generation
    """

    topic: str = Field(
        description="The main topic for presentation generation",
        min_length=3,
        max_length=200,
    )

    customization: Optional[ContentCustomizationParams] = Field(
        default_factory=ContentCustomizationParams,
        description="Content customization parameters",
    )

    class Config:
        schema_extra = {
            "example": {
                "topic": "Artificial Intelligence in Healthcare",
                "customization": {
                    "tone": "professional",
                    "length": "descriptive",
                    "range": "10-15",
                    "target_audience": "technical_experts",
                    "presentation_purpose": "conference_talk",
                    "detail_level": "deep_dive",
                    "include_examples": "extensive",
                    "engagement_level": "highly_engaging",
                    "industry": "healthcare",
                    "data_focus": "data_driven",
                    "include_call_to_action": False,
                },
            }
        }
