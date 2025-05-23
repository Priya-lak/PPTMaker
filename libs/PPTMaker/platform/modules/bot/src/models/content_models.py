from typing import Annotated, List, Literal, Union

from pydantic import BaseModel, Field


class ContentPage(BaseModel):
    type: Literal[
        "content_page",
        "title_page",
    ]
    title: str
    bullet_points: List[str] | None


class ImagePage(BaseModel):
    type: Literal[
        "image_page",
        "image_content_page",
    ]
    title: str
    image_search_keyword: str
    image_description: str
    caption: str
    layout: Literal["side_by_side", "image_bottom", "image_title_caption", "standard"]


class FirstPage(BaseModel):
    type: Literal["first_page"]
    title: str
    description: str


class PresentationModel(BaseModel):
    title_page: FirstPage
    presentation_content: List[
        Annotated[Union[ContentPage, ImagePage], Field(discriminator="type")]
    ]
