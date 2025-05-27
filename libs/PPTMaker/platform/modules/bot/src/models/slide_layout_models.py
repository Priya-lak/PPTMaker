from typing import Annotated, List, Literal, Union

from pydantic import BaseModel, Field


class TitleSlideModel(BaseModel):
    layout: Literal["TITLE"]
    title: str


class ContentSlideModel(BaseModel):
    layout: Literal["TITLE_AND_CONTENT"]
    title: str
    points: List[str]


class SectionHeaderSlideModel(BaseModel):
    layout: Literal["SECTION_HEADER"]
    title: str
    subtitle: str


class TwoContentSlideModel(BaseModel):
    layout: Literal["TWO_CONTENT"]
    title: str
    left_points: List[str]
    right_points: List[str]


class ComparisonSlideModel(BaseModel):
    layout: Literal["COMPARISON"]
    title: str
    left_heading: str
    right_heading: str
    left_points: List[str]
    right_points: List[str]


class TitleOnlySlideModel(BaseModel):
    layout: Literal["TITLE_ONLY"]
    title: str


class BlankTitleSlideModel(BaseModel):
    layout: Literal["BLANK"]
    title: str
    subtitle: str


class ContentCaptionSlideModel(BaseModel):
    layout: Literal["CONTENT_WITH_CAPTION"]
    title: str
    points: List[str]


class PresentationModel(BaseModel):
    title: str
    presentation_content: List[
        Annotated[
            Union[
                ContentCaptionSlideModel,
                BlankTitleSlideModel,
                TitleOnlySlideModel,
                ComparisonSlideModel,
                TwoContentSlideModel,
                SectionHeaderSlideModel,
                ContentSlideModel,
                TitleSlideModel,
            ],
            Field(discriminator="layout"),
        ]
    ]
