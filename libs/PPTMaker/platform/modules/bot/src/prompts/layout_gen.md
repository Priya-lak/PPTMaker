# PowerPoint Content Generation Prompt

Generate structured content for PowerPoint presentations using the specified layouts and placeholders. Content should be professionally formatted and comprehensively utilize all provided source material.

## Core Requirements

### Layout Compliance
- **MANDATORY**: Use ONLY the provided layouts and their exact placeholders
                or I WILL KIDNAP YOUR FAMILY
- **MANDATORY**: Use exact `idx` values and placeholder names as specified
- **FORBIDDEN**: Creating additional placeholders or modifying layout structure

### Content Coverage
- Utilize virtually ALL provided source material within the presentation
- Distribute content strategically across slides to ensure comprehensive coverage
- No significant portions of source material should remain unused

## Content Guidelines by Placeholder Type

### Titles (Title, Vertical Title)
- **Length**: 5-10 words maximum
- **Style**: Concise, descriptive, actionable
- **Format**: Clear headers that summarize section content

### Content (Content, Vertical Text)
- **Length**: Under 150 words per placeholder
- **Format**: Bullet points for lists, short paragraphs for descriptions
- **Style**: Start bullet points with action verbs or key concepts
- **Tone**: Professional and engaging

### Subtitles/Captions (Subtitle, Text)
- **Purpose**: Supporting context or explanatory information
- **Length**: 1-2 sentences for captions, longer for descriptive text
- **Style**: Complement main content without redundancy

## Layout Diversity Strategy

Maximize visual interest by utilizing varied positioning patterns:

**Spatial Arrangements**:
- Vertical flows (top-to-bottom)
- Horizontal layouts (side-by-side)
- Multi-column distributions
- Corner/quadrant positioning
- Center-focused with surrounding elements
- Asymmetrical distributions

**Content Emphasis**:
- Header-heavy (prominent titles)
- Content-rich (multiple content blocks)
- Balanced title-to-content ratios

## Required JSON Structure

```json
{
    "title": "presentation_title",
    "slides": [
        {
            "layout": "layout_name",
            "placeholders": {
                "idx_1": "content_text",
                "idx_2": "content_text",
                "idx_3": "content_text"
            }
        }
    ]
}
```

### JSON Requirements
- Valid format with proper quotes and commas
- Each slide must include both "layout" and "placeholders" properties
- All placeholder content must be strings
- Keys must be exact `idx` values from layout specifications

## Layout Input Format

Layout is as such:
{slide_layouts}

## Main content
Adhere to the content provided here:
{content}

## Content Formatting Guidelines

- **Lists**: Use bullet points with `•` symbol
- **Line breaks**: Use `\\n` for multi-line content
- **Emphasis**: Keep formatting simple and readable
- **Consistency**: Maintain uniform style across all slides

## Prohibited Content Types

- Comparison slides or side-by-side evaluations
- Made-up layout names or placeholder modifications
- Content that significantly deviates from source material
- Overly lengthy individual content blocks

## Quality Standards

1. **Comprehensiveness**: All source material strategically incorporated
2. **Clarity**: Each placeholder serves a distinct purpose
3. **Professional tone**: Business-appropriate language and structure
4. **Visual variety**: Diverse layout utilization throughout presentation
5. **Logical flow**: Content progression that supports overall narrative

---

**Process**: Analyze provided source material → Select appropriate layout variety → Distribute content strategically → Format according to placeholder types → Validate JSON structure
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
