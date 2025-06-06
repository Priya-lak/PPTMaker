# Utility function to convert params to prompt string
from pydantic import BaseModel


def params_to_prompt_string(params: BaseModel) -> str:
    """
    Convert customization parameters to a formatted string for AI prompt.
    Only includes parameters that are not None.
    """
    prompt_parts = []
    params_dict = params.model_dump()
    for attr, val in params_dict.items():
        prompt_parts.append(f"**{attr.capitalize()}**: {val}")
    return "\n".join(prompt_parts)
