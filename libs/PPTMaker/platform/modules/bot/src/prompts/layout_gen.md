# PowerPoint Content Generation Prompt

Please generate content for a PowerPoint presentation in the following JSON format. The content should be structured to match PowerPoint slide layouts and their placeholders.


---

## Required JSON Structure:
```json
{
    "slides": [
        {
            "layout": "layout_name",
            "placeholders": {
                "placeholder_name_1": "content_text",
                "placeholder_name_2": "content_text",
                "placeholder_name_3": "content_text"
            }
        },
        {
            "layout": "another_layout_name",
            "placeholders": {
                "placeholder_name_1": "content_text",
                "placeholder_name_2": "content_text"
            }
        }
    ]
}
```

## Content Guidelines:

1. **Titles**: Keep concise and descriptive (5-10 words)
2. **Content**: Use bullet points for lists, short paragraphs for descriptions
3. **Bullet Points**: Start with action verbs or key concepts
4. **Length**: Keep individual content blocks under 150 words
5. **Tone**: Professional and engaging

## Important Notes:
- Always wrap the slides array in a "slides" property
- Ensure valid JSON format with proper quotes and commas
- Each slide must have both "layout" and "placeholders" properties
- All placeholder content must be strings

## Example Response:
### Example layout:
If the layout is something like this:

```json

 [

  {
    "layout": "Title Slide",
    "placeholders": ["Title 1",
                   "Subtitle 2",]
  },
  {
    "layout": "Title and Content",
    "placeholders": ["Title 1",
                   "Title and Content",]
  }
]

```


### Expected output
```json
{
    "slides": [
        {
            "layout": "Title Slide",
            "placeholders": {
                "Title 1": "Introduction to Machine Learning",
                "Subtitle 2": "Fundamentals and Applications"
            }
        },
        {
            "layout": "Title and Content",
            "placeholders": {
                "Title 1": "What is Machine Learning?",
                "Content Placeholder 2": "• A subset of artificial intelligence\\n• Enables systems to learn from data\\n• Makes predictions without explicit programming"
            }
        }
    ]
}
```
