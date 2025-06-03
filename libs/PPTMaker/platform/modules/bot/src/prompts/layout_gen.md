# PowerPoint Content Generation Prompt

Please generate content for a PowerPoint presentation in the following JSON format. The content should be structured to match PowerPoint slide layouts and their placeholders.
**Make sure to use all the the provided content inside the layout content. Structure the layout in such a way that all the content can fit easily into the presentation**
---

## Required JSON Structure:
```json
{
    "title":"title",
    "slides": [
        {
            "layout": "layout_name",
            "placeholders": {
                "idx_1": "content_text",
                "idx_2": "content_text",
                "idx_3": "content_text"
            }
        },
        {
            "layout": "another_layout_name",
            "placeholders": {
                "idx_1": "content_text",
                "idx_2": "content_text"
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
- All placeholder content must be strings, the keys must be the exact idx values provided

## Example Response:
### Example layout:
If the layout is something like this:

```json

 [

  {
    "layout": "Title Slide",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Subtitle 2"},]
  },
  {
    "layout": "Title and Content",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Title and Content"},]
  }
]

```


### Expected output
```json
{
    "title":"Title",
    "slides": [
        {
            "layout": "Title Slide",
            "placeholders": {
                "0": "Introduction to Machine Learning",
                "1": "Fundamentals and Applications"
            }
        },
        {
            "layout": "Title and Content",
            "placeholders": {
                "0": "What is Machine Learning?",
                "1": "• A subset of artificial intelligence\\n• Enables systems to learn from data\\n• Makes predictions without explicit programming"
            }
        }
    ]
}
```
