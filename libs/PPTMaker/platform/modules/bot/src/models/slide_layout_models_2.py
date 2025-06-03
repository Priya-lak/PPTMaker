import json
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


# Model for individual slide content
class SlideContent(BaseModel):
    layout: str = Field(
        ..., min_length=1, description="Exact layout name from available layouts"
    )
    placeholders: Dict[str, str] = Field(
        ..., min_items=1, description="Mapping of placeholder names to content"
    )


# Model for the complete presentation response
class PresentationResponse(BaseModel):
    title: str
    slides: List[SlideContent] = Field(
        ..., min_items=1, description="List of slides with their content"
    )


# Model for layout definition (for input validation)
class LayoutDefinition(BaseModel):
    layout: str = Field(..., min_length=1, description="Layout name")
    placeholders: List[Dict] = Field(
        ..., min_items=1, description="List of placeholder names"
    )

    @field_validator("layout")
    def name_not_empty(cls, v):
        return v.strip()


# Model for available layouts input
class AvailableLayouts(BaseModel):
    available_layouts: List[LayoutDefinition] = Field(..., min_items=1)


# Validation class with helper methods
class PPTValidator:
    @staticmethod
    def validate_response(json_data: str) -> PresentationResponse:
        """Validate JSON response from AI"""
        try:
            data = json.loads(json_data) if isinstance(json_data, str) else json_data

            # Handle both list format and object format
            if isinstance(data, list):
                slides_data = data
            elif isinstance(data, dict) and "slides" in data:
                slides_data = data["slides"]
            else:
                slides_data = data

            slides = [SlideContent(**slide) for slide in slides_data]
            return PresentationResponse(slides=slides)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")
        except Exception as e:
            raise ValueError(f"Validation error: {e}")

    @staticmethod
    def validate_against_layouts(
        response: PresentationResponse, available_layouts: AvailableLayouts
    ) -> bool:
        """Validate that response uses only available layouts and placeholders"""
        layout_dict = {
            layout.name: layout.placeholders
            for layout in available_layouts.available_layouts
        }

        for slide in response.slides:
            # Check if layout exists
            if slide.layout not in layout_dict:
                raise ValueError(f"Layout '{slide.layout}' is not in available layouts")

            # Check if all placeholders are valid for this layout
            available_placeholders = set(layout_dict[slide.layout])
            used_placeholders = set(slide.placeholders.keys())

            invalid_placeholders = used_placeholders - available_placeholders
            if invalid_placeholders:
                raise ValueError(
                    f"Invalid placeholders for layout '{slide.layout}': {invalid_placeholders}"
                )

        return True
