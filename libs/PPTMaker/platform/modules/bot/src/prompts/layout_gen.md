# PowerPoint Content Generation Prompt

Please generate content for a PowerPoint presentation in the following JSON format. The content should be structured to match PowerPoint slide layouts and their placeholders.

**CRITICAL REQUIREMENTS**:

- You must use virtually ALL the provided content within the presentation slides. Structure the layout distribution strategically to ensure comprehensive coverage of the source material without leaving significant portions unused.
- For each layout, ONLY use the placeholders and the idxs provided. Do not use additional placeholder ids for the layouts.[ e.g. if a particular layout has only 3 placeholder *DO NOT add more than 3 placeholders.*. Use the exact idx and placeholder provided].
- use only the layouts and their respective placeholders provided.
- DO NOT make up layout names or placeholders OR ELSE I WILL KIDNAP YOUR FAMILY

## Layout structure:
{slide_layouts}
---

## Required JSON Structure:
```json
{
    "title":"presentation_title",
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
6. **Content Coverage**: Ensure comprehensive utilization of provided material
7. **Avoid Comparisons**: Do not create comparison slides or side-by-side evaluations

## Layout Diversity Requirements:

Utilize a wide variety of slide layouts to create visual interest and accommodate different content types. Distribute content across diverse positioning patterns including:

- **Vertical layouts**: Top-to-bottom content flow
- **Horizontal layouts**: Side-by-side content arrangement
- **Multi-column layouts**: Three or more content sections
- **Corner positioning**: Content in specific quadrants
- **Center-focused layouts**: Central content with surrounding elements
- **Asymmetrical layouts**: Uneven content distribution
- **Header-heavy layouts**: Prominent titles with supporting content below
- **Content-rich layouts**: Multiple content blocks with minimal titles

## Important Notes:
- Always wrap the slides array in a "slides" property
- Ensure valid JSON format with proper quotes and commas
- Each slide must have both "layout" and "placeholders" properties
- All placeholder content must be strings, the keys must be the exact idx values provided
- Maximize content utilization from source material
- Vary slide layouts' positioning significantly throughout the presentation

## Example Responses:

### Example Layout Set 1:
```json
[
  {
    "layout": "Title Slide",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Subtitle 2"}]
  },
  {
    "layout": "Two Content",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Content 2"},
                   {"idx":2,"name":"Content 3"}]
  },
  {
    "layout": "Content with Caption",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Content 2"},
                   {"idx":2,"name":"Text 3"}]
  }
]
```

### Expected Output 1:
```json
{
    "title":"Digital Marketing Strategy",
    "slides": [
        {
            "layout": "Title Slide",
            "placeholders": {
                "0": "Digital Marketing Strategy 2025",
                "1": "Comprehensive Guide to Modern Marketing"
            }
        },
        {
            "layout": "Two Content",
            "placeholders": {
                "0": "Social Media Platforms",
                "1": "• Instagram: Visual storytelling and engagement\\n• LinkedIn: Professional networking and B2B\\n• TikTok: Short-form video content\\n• Twitter: Real-time updates and conversations",
                "2": "• Facebook: Community building and advertising\\n• YouTube: Long-form video content\\n• Pinterest: Visual discovery and inspiration\\n• Snapchat: Ephemeral content and AR features"
            }
        },
        {
            "layout": "Content with Caption",
            "placeholders": {
                "0": "Email Marketing Best Practices",
                "1": "• Personalization increases open rates by 26%\\n• Segment audiences based on behavior\\n• A/B test subject lines and content\\n• Optimize for mobile devices\\n• Include clear call-to-action buttons",
                "2": "Email remains one of the highest ROI marketing channels with an average return of $42 for every $1 spent"
            }
        }
    ]
}
```

### Example Layout Set 2:
```json
[
  {
    "layout": "Section Header",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Text 2"}]
  },
  {
    "layout": "Four Content",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Content 2"},
                   {"idx":2,"name":"Content 3"},
                   {"idx":3,"name":"Content 4"},
                   {"idx":4,"name":"Content 5"}]
  },
  {
    "layout": "Title Only",
    "placeholders": [{"idx":0,"name":"Title 1"}]
  },
  {
    "layout": "Blank",
    "placeholders": [{"idx":0,"name":"Text 1"}]
  }
]
```

### Expected Output 2:
```json
{
    "title":"Project Management Methodologies",
    "slides": [
        {
            "layout": "Section Header",
            "placeholders": {
                "0": "Agile Development Framework",
                "1": "Iterative approach to software development emphasizing flexibility and customer collaboration"
            }
        },
        {
            "layout": "Four Content",
            "placeholders": {
                "0": "Agile Methodology Components",
                "1": "Sprint Planning\\n• Define goals and scope\\n• Estimate effort required\\n• Assign team responsibilities",
                "2": "Daily Standups\\n• Progress updates\\n• Identify blockers\\n• Coordinate team activities",
                "3": "Sprint Reviews\\n• Demonstrate completed work\\n• Gather stakeholder feedback\\n• Plan next iteration",
                "4": "Retrospectives\\n• Reflect on process improvements\\n• Address team challenges\\n• Celebrate successes"
            }
        },
        {
            "layout": "Title Only",
            "placeholders": {
                "0": "Implementation Strategy"
            }
        },
        {
            "layout": "Blank",
            "placeholders": {
                "0": "Successful agile implementation requires strong team communication, clear documentation, and continuous adaptation to changing requirements. Organizations typically see 25-30% improvement in project delivery times when properly implementing agile methodologies with dedicated scrum masters and product owners."
            }
        }
    ]
}
```

### Example Layout Set 3:
```json
[
  {
    "layout": "Picture with Caption",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Content 2"},
                   {"idx":2,"name":"Text 3"}]
  },
  {
    "layout": "Vertical Title and Text",
    "placeholders": [{"idx":0,"name":"Vertical Title 1"},
                   {"idx":1,"name":"Vertical Text 2"}]
  },
  {
    "layout": "Title and Vertical Text",
    "placeholders": [{"idx":0,"name":"Title 1"},
                   {"idx":1,"name":"Vertical Text 2"}]
  }
]
```

### Expected Output 3:
```json
{
    "title":"Sustainable Energy Solutions",
    "slides": [
        {
            "layout": "Picture with Caption",
            "placeholders": {
                "0": "Renewable Energy Sources",
                "1": "• Solar panels convert sunlight to electricity\\n• Wind turbines harness kinetic energy\\n• Hydroelectric systems use water flow\\n• Geothermal taps earth's internal heat",
                "2": "Renewable energy capacity has grown 260% globally since 2010"
            }
        },
        {
            "layout": "Vertical Title and Text",
            "placeholders": {
                "0": "Energy Storage Technologies",
                "1": "Battery technology advances enable better grid storage. Lithium-ion batteries provide efficient short-term storage while pumped hydro offers large-scale solutions. Emerging technologies include compressed air systems and molten salt thermal storage for extended duration applications."
            }
        },
        {
            "layout": "Title and Vertical Text",
            "placeholders": {
                "0": "Implementation Challenges",
                "1": "Infrastructure modernization requires significant investment. Grid integration poses technical challenges. Regulatory frameworks need updating. Public acceptance varies by region. Training workforce for new technologies essential."
            }
        }
    ]
}
```
