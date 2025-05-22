from typing import List, Literal, Union
from pydantic import BaseModel

class ContentPage(BaseModel):
    type: Literal["content_page","title_page"]
    title: str
    bullet_points: List[str]|None

class FirstPage(BaseModel):
    type: Literal["first_page"]
    title: str
    description: str


class PresentationModel(BaseModel):
    title_page: FirstPage
    presentation_content: List[ContentPage]