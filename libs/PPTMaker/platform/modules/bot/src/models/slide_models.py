from typing import Optional

from pydantic import BaseModel, Field


class ShapePosition(BaseModel):
    top: float = Field(..., description="Distance from the top of the slide in inches")
    left: float = Field(
        ..., description="Distance from the left of the slide in inches"
    )
    width: Optional[float] = Field(
        None, description="Width of the image in inches (optional)"
    )
    height: Optional[float] = Field(
        None, description="Height of the image in inches (optional)"
    )


class ImageSlideLayouts(BaseModel):
    pass
