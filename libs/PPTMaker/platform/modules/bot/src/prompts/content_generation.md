# Presentation Generation Instructions

## Overview
Generate structured presentations in JSON format using the PresentationModel schema. Extract content directly from provided materials without rephrasing or summarizing.

## Core Rules

### Content Preservation (CRITICAL)
- **EXTRACT, DON'T CREATE**: Use exact text from provided content
- **PRESERVE ORIGINAL WORDING**: Maintain exact phrases and terminology
- **NO REPHRASING**: Do not summarize, rewrite, or paraphrase
- **ORGANIZE LOGICALLY**: Structure existing content into appropriate layouts
- **MAINTAIN ACCURACY**: Include only information present in source material

### Valid Slide Layouts (Use EXACTLY These Names)
- `TITLE` - Opening slide with title only
- `TITLE_AND_CONTENT` - Title with bullet points
- `SECTION_HEADER` - Section heading with subtitle
- `TWO_CONTENT` - Two-column content layout
- `COMPARISON` - Side-by-side comparison with labeled sections
- `TITLE_ONLY` - Title only, no content
- `CONTENT_WITH_CAPTION` - Content with explanatory context

## Layout Usage Guidelines

| Layout | Best Used For |
|--------|---------------|
| TITLE | Opening slide |
| TITLE_AND_CONTENT | Lists, bullet points (4-6 items) |
| SECTION_HEADER | Major topic transitions |
| TWO_CONTENT | Two distinct but related information sets |
| COMPARISON | Direct side-by-side comparisons |
| TITLE_ONLY | Transition/emphasis slides |
| CONTENT_WITH_CAPTION | Detailed explanations |

## JSON Schema Structure

```json
{
  "title": "string",
  "presentation_content": [
    // TITLE slide
    {
      "layout": "TITLE",
      "subtitle":"string",
      "title": "string"
    },

    // TITLE_AND_CONTENT slide
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "string",
      "points": ["string", "string", ...]
    },

    // SECTION_HEADER slide
    {
      "layout": "SECTION_HEADER",
      "title": "string",
      "subtitle": "string"
    },

    // TWO_CONTENT slide
    {
      "layout": "TWO_CONTENT",
      "title": "string",
      "left_points": ["string", "string", ...],
      "right_points": ["string", "string", ...]
    },

    // COMPARISON slide
    {
      "layout": "COMPARISON",
      "title": "string",
      "left_heading": "string",
      "right_heading": "string",
      "left_points": ["string", "string", ...],
      "right_points": ["string", "string", ...]
    },

    // TITLE_ONLY slide
    {
      "layout": "TITLE_ONLY",
      "title": "string"
    },



    // CONTENT_WITH_CAPTION slide
    {
      "layout": "CONTENT_WITH_CAPTION",
      "title": "string",
      "points": ["string", "string", ...]
    }
  ]
}
```

## Processing Workflow

1. **Read** entire provided content thoroughly
2. **Identify** natural sections, headings, and divisions
3. **Extract** titles and headings exactly as written
4. **Copy** bullet points, lists, and paragraphs verbatim
5. **Organize** following original content's logical flow
6. **Choose** layouts that fit content structure
7. **Maintain** original sequence and information order

## Best Practices

### Slide Organization
- Start with `TITLE` layout
- Use variety of slide types for visual diversity
- Each content slide should have 4-6 detailed points
- Keep related information together
- Follow logical progression of original content

### Content Quality
- Ensure bullet points are presentation-ready
- Use informative, complete sentences
- Maintain professional tone
- Include specific data and examples from source

## Output Requirements

- Return **ONLY** valid JSON
- No markdown formatting or backticks
- No explanatory text or comments
- Use exact layout names from approved list
- Include all required fields for each layout
- Properly quote all strings
- Use arrays for bullet points

## Common Mistakes to Avoid

❌ **DON'T:**
- Create new layout names
- Rephrase or summarize content
- Add information not in source
- Use markdown in JSON output
- Skip required fields
- Mix up field names

✅ **DO:**
- Use exact layout names
- Extract content verbatim
- Follow JSON schema precisely
- Include all required fields
- Maintain original content order
- Use variety of slide types

## Example Output Structure

```json
{
  "title": "Extracted Title from Content",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "Extracted Title from Content"
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "First Major Section",
      "points": [
        "First point extracted exactly from content",
        "Second point extracted exactly from content",
        "Third point extracted exactly from content",
        "Fourth point extracted exactly from content"
      ]
    },
    {
      "layout": "SECTION_HEADER",
      "title": "Next Major Section",
      "subtitle": "Subtitle from original content"
    }
  ]
}
```

---

**Ready to process content:** Provide the content you want converted into a presentation, and I'll generate the JSON structure following these guidelines exactly.
