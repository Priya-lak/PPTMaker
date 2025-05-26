## **Instructions**

You will be given a **topic**. Based on that topic, generate a structured presentation in JSON format using the **PresentationModel** schema below. Each slide must adhere to one of the specified layout models.

---

## **Slide Layout Options (Enum: SlideLayout)**

Each slide must conform to one of these layouts:

* `TITLE`: Title slide
* `TITLE_AND_CONTENT`: Content with bullet points
* `SECTION_HEADER`: Section heading with subtitle
* `TWO_CONTENT`: Two-column content
* `COMPARISON`: Side-by-side comparison with labeled sections
* `TITLE_ONLY`: Title only (no content)
* `BLANK`: Blank slide with title and subtitle
* `CONTENT_WITH_CAPTION`: Content + long caption paragraph

---

## **Guidelines:**

* Keep the presentation between **5 to 7 slides total**
* Start with a `TITLE` layout for the opening slide
* Use a **mix** of slide types for visual and informational diversity
* Ensure bullet points are informative and presentation-ready
* Use `CONTENT_WITH_CAPTION` layout where a visual explanation or long paragraph would be appropriate
* Use `SECTION_HEADER` or `TITLE_ONLY` to break content flow or introduce a new segment
* Each content slide should have **4–6 detailed bullet points**
* Avoid repeating slide types too often
* Organize content logically and clearly

---

## **Output Format**

Return your result as a JSON object using the schema below. **Do not** include any markdown, backticks, or explanatory text. Just return a valid JSON object.

```python
class TitleSlideModel(BaseModel):
    layout: Literal[SlideLayout.TITLE]
    title: str

class ContentSlideModel(BaseModel):
    layout: Literal[SlideLayout.TITLE_AND_CONTENT]
    title: str
    points: List[str]

class SectionHeaderSlideModel(BaseModel):
    layout: Literal[SlideLayout.SECTION_HEADER]
    title: str
    subtitle: str

class TwoContentSlideModel(BaseModel):
    layout: Literal[SlideLayout.TWO_CONTENT]
    title: str
    left_points: List[str]
    right_points: List[str]

class ComparisonSlideModel(BaseModel):
    layout: Literal[SlideLayout.COMPARISON]
    title: str
    left_heading: str
    right_heading: str
    left_points: List[str]
    right_points: List[str]

class TitleOnlySlideModel(BaseModel):
    layout: Literal[SlideLayout.TITLE_ONLY]
    title: str

class BlankTitleSlideModel(BaseModel):
    layout: Literal[SlideLayout.BLANK]
    title: str
    subtitle: str

class ContentCaptionSlideModel(BaseModel):
    layout: Literal[SlideLayout.CONTENT_WITH_CAPTION]
    title: str
    points: List[str]

class PresentationModel(BaseModel):
    title:str
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
                TitleSlideModel
            ],
            Field(discriminator="layout")
        ]
    ]
```

---

## **Example Output for Topic: “Climate Change Solutions”**

```json
{
  "title":"Climate Change: Solutions for a Sustainable Future",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "Climate Change: Solutions for a Sustainable Future"
    },
    {
      "layout": "CONTENT_WITH_CAPTION",
      "title": "The Climate Crisis",
      "points": ["Global warming accelerates ice melt, rising sea levels, and extreme weather". "Annual global temperatures continue to break historical records",  "widespread environmental and economic impacts already visible across continents."]
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Renewable Energy Innovations",
      "points": [
        "Solar energy costs have dropped by 90% over the last decade",
        "Wind power now supports over 130 million homes annually",
        "Battery storage tech enables 24/7 renewable energy delivery",
        "Green hydrogen serves as a clean fuel for heavy industries",
        "Smart grids reduce power waste using AI-driven optimization"
      ]
    },
    {
      "layout": "COMPARISON",
      "title": "Carbon Capture: Natural vs Technological",
      "left_heading": "Natural Solutions",
      "right_heading": "Technological Methods",
      "left_points": [
        "Afforestation and reforestation",
        "Soil carbon sequestration",
        "Wetland restoration",
        "Agroforestry techniques"
      ],
      "right_points": [
        "Direct air capture systems",
        "Carbon capture and storage (CCS)",
        "Enhanced mineral weathering",
        "Bioenergy with CCS (BECCS)"
      ]
    },
    {
      "layout": "TWO_CONTENT",
      "title": "Policy and Personal Action",
      "left_points": [
        "National carbon pricing initiatives",
        "International climate agreements (e.g., Paris Accord)",
        "Subsidies for green technology adoption",
        "Infrastructure investment in clean transit"
      ],
      "right_points": [
        "Use public transport or electric vehicles",
        "Shift to a plant-based diet",
        "Improve home energy efficiency",
        "Support sustainable brands and products"
      ]
    },
    {
      "layout": "SECTION_HEADER",
      "title": "Future Outlook",
      "subtitle": "A path toward global sustainability"
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Next Steps and Global Coordination",
      "points": [
        "UN-led climate summits to align national strategies",
        "Investment in global renewable infrastructure",
        "Stronger accountability for emissions targets",
        "Education and climate literacy programs",
        "Research into climate-resilient agriculture and energy"
      ]
    }
  ]
}
```
