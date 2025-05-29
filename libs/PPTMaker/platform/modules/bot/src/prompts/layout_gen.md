# PowerPoint Content Generation Prompt

Please generate content for a PowerPoint presentation in the following JSON format. The content should be structured to match PowerPoint slide layouts and their placeholders.

## Required JSON Structure:
```json
[
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
```

## Layout Types and Common Placeholders:

### Title Slide
- **Layout**: "Title Slide"
- **Common Placeholders**:
  - "Title 1": Main presentation title
  - "Subtitle 2": Subtitle or presenter information

### Title and Content
- **Layout**: "Title and Content"
- **Common Placeholders**:
  - "Title 1": Slide title
  - "Content Placeholder 2": Main content (bullet points, paragraphs)

### Section Header
- **Layout**: "Section Header"
- **Common Placeholders**:
  - "Title 1": Section title
  - "Text Placeholder 2": Section description

### Two Content
- **Layout**: "Two Content"
- **Common Placeholders**:
  - "Title 1": Slide title
  - "Content Placeholder 2": Left content
  - "Content Placeholder 3": Right content

### Comparison
- **Layout**: "Comparison"
- **Common Placeholders**:
  - "Title 1": Slide title
  - "Text Placeholder 2": Left comparison title
  - "Content Placeholder 3": Left comparison content
  - "Text Placeholder 4": Right comparison title
  - "Content Placeholder 5": Right comparison content

### Content with Caption
- **Layout**: "Content with Caption"
- **Common Placeholders**:
  - "Title 1": Slide title
  - "Content Placeholder 2": Main content
  - "Text Placeholder 3": Caption text

## Content Guidelines:

1. **Titles**: Keep concise and descriptive (5-10 words)
2. **Content**: Use bullet points for lists, short paragraphs for descriptions
3. **Bullet Points**: Start with action verbs or key concepts
4. **Length**: Keep individual content blocks under 150 words
5. **Tone**: Professional and engaging

## Example Request Format:

"Create a 5-slide presentation about [TOPIC] with the following structure:
- Title slide
- Overview/agenda slide
- 2-3 content slides covering main points
- Conclusion/next steps slide

Topic: [YOUR_SPECIFIC_TOPIC]
Audience: [TARGET_AUDIENCE]
Purpose: [PRESENTATION_PURPOSE]

Please provide the content in the JSON format specified above."

---

**Instructions for Use:**
Replace the bracketed placeholders with your specific requirements and paste this prompt along with your topic details to generate structured PowerPoint content.
