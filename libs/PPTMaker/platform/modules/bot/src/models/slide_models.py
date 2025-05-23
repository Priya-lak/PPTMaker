from enum import IntEnum
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


class SlideLayout(IntEnum):
    TITLE = 0
    TITLE_AND_CONTENT = 1
    SECTION_HEADER = 2
    TWO_CONTENT = 3
    COMPARISON = 4
    TITLE_ONLY = 5
    BLANK = 6
    CONTENT_WITH_CAPTION = 7
    PICTURE_WITH_CAPTION = 8
