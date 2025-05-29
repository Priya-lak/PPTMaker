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

    # @field_validator("layout")
    # def layout_not_empty(cls, v):
    #     if not v.strip():
    #         raise ValueError("Layout name cannot be empty or whitespace only")
    #     return v.strip()

    # @field_validator("placeholders")
    # def validate_placeholders(cls, v):
    #     if not v:
    #         raise ValueError("At least one placeholder must be provided")

    #     # Validate each placeholder
    #     for placeholder_name, content in v.items():
    #         if not placeholder_name.strip():
    #             raise ValueError("Placeholder name cannot be empty")
    #         if not isinstance(content, str):
    #             raise ValueError("Placeholder content must be a string")
    #         if len(content.strip()) == 0:
    #             raise ValueError(
    #                 f'Content for placeholder "{placeholder_name}" cannot be empty'
    #             )
    #         if len(content) > 1000:  # Reasonable limit for slide content
    #             raise ValueError(
    #                 f'Content for placeholder "{placeholder_name}" exceeds 1000 characters'
    #             )

    #     return v


# Model for the complete presentation response
class PresentationResponse(BaseModel):
    slides: List[SlideContent] = Field(
        ..., min_items=1, description="List of slides with their content"
    )

    # @field_validator("slides")
    # def validate_slides(cls, v):
    #     if len(v) == 0:
    #         raise ValueError("At least one slide must be provided")
    #     if len(v) > 50:  # Reasonable limit for presentation length
    #         raise ValueError("Presentation cannot exceed 50 slides")
    #     return v


# Model for layout definition (for input validation)
class LayoutDefinition(BaseModel):
    layout: str = Field(..., min_length=1, description="Layout name")
    placeholders: List[str] = Field(
        ..., min_items=1, description="List of placeholder names"
    )

    @field_validator("layout")
    def name_not_empty(cls, v):
        return v.strip()

    # @field_validator("placeholders")
    # def validate_placeholder_names(cls, v):
    #     if not v:
    #         raise ValueError("At least one placeholder must be defined")

    #     cleaned_placeholders = []
    #     for placeholder in v:
    #         if not isinstance(placeholder, str):
    #             raise ValueError("Placeholder names must be strings")
    #         cleaned = placeholder.strip()
    #         if not cleaned:
    #             raise ValueError("Placeholder names cannot be empty")
    #         cleaned_placeholders.append(cleaned)

    #     # Check for duplicates
    #     if len(cleaned_placeholders) != len(set(cleaned_placeholders)):
    #         raise ValueError("Duplicate placeholder names are not allowed")

    #     return cleaned_placeholders


# Model for available layouts input
class AvailableLayouts(BaseModel):
    available_layouts: List[LayoutDefinition] = Field(..., min_items=1)

    # @model_validator
    # def validate_unique_layout_names(cls, values):
    #     layouts = values.get("available_layouts", [])
    #     layout_names = [layout.name for layout in layouts]
    #     if len(layout_names) != len(set(layout_names)):
    #         raise ValueError("Duplicate layout names are not allowed")
    #     return values


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


# Example usage function
def example_usage():
    # Example JSON response validation
    json_response = """
    [
        {
            "layout": "Title Slide",
            "placeholders": {
                "Title 1": "My Presentation",
                "Subtitle 2": "A comprehensive overview"
            }
        },
        {
            "layout": "Title and Content",
            "placeholders": {
                "Title 1": "Key Points",
                "Content Placeholder 2": "• Point 1\\n• Point 2\\n• Point 3"
            }
        }
    ]
    """

    try:
        validated_response = PPTValidator.validate_response(json_response)
        print("✅ Response validation successful!")
        print(f"Number of slides: {len(validated_response.slides)}")

        # Example layout validation
        layouts = AvailableLayouts(
            available_layouts=[
                LayoutDefinition(
                    name="Title Slide", placeholders=["Title 1", "Subtitle 2"]
                ),
                LayoutDefinition(
                    name="Title and Content",
                    placeholders=["Title 1", "Content Placeholder 2"],
                ),
            ]
        )

        PPTValidator.validate_against_layouts(validated_response, layouts)
        print("✅ Layout validation successful!")

    except ValueError as e:
        print(f"❌ Validation failed: {e}")


if __name__ == "__main__":
    example_usage()
