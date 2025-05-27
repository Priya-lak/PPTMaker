# Utility function to convert params to prompt string
from libs.PPTMaker.platform.modules.bot.src.models.custom_content_models import (
    ContentCustomizationParams,
)


def params_to_prompt_string(params: ContentCustomizationParams) -> str:
    """
    Convert customization parameters to a formatted string for AI prompt.
    Only includes parameters that are not None.
    """
    field_map = {
        "tone": "TONE",
        "length": "LENGTH",
        "slide_range": "RANGE",
        "target_audience": "TARGET_AUDIENCE",
        "presentation_purpose": "PRESENTATION_PURPOSE",
        "detail_level": "DETAIL_LEVEL",
        "include_examples": "INCLUDE_EXAMPLES",
        "engagement_level": "ENGAGEMENT_LEVEL",
        "industry": "INDUSTRY",
        "visual_preference": "VISUAL_PREFERENCE",
        "data_focus": "DATA_FOCUS",
        "regional_focus": "REGIONAL_FOCUS",
        "time_duration": "TIME_DURATION",
        "include_call_to_action": "INCLUDE_CALL_TO_ACTION",
        "branded_content": "BRANDED_CONTENT",
        "specific_requirements": "SPECIFIC_REQUIREMENTS",
        "avoid_topics": "AVOID_TOPICS",
    }

    prompt_parts = []
    for attr, label in field_map.items():
        value = getattr(params, attr, None)
        if value is not None:
            # Use .value if the attribute has it (likely an Enum), else use the value directly
            prompt_value = getattr(value, "value", value)
            prompt_parts.append(f"**{label}**: {prompt_value}")

    return "\n".join(prompt_parts)
