# **Instructions**

You will be given content. Based on that descriptive content, generate a structured presentation in JSON format using the **PresentationModel** schema below. Each slide must adhere to one of the specified layout models. Be sure to use only the content given to you inside as values in the structure. Try to match the content as close as possible.

**CRITICAL CONTENT RULE: You MUST use the exact text, phrases, and information from the provided content. Do NOT rephrase, summarize, or rewrite the content. Extract and organize the existing text directly into the appropriate slide layouts.**
---

## **CRITICAL: Valid Slide Layout Options**

Each slide must use EXACTLY ONE of these layout values. **DO NOT CREATE OR USE ANY OTHER LAYOUT NAMES:**

* `TITLE` - Title slide only
* `TITLE_AND_CONTENT` - Content with bullet points
* `SECTION_HEADER` - Section heading with subtitle
* `TWO_CONTENT` - Two-column content
* `COMPARISON` - Side-by-side comparison with labeled sections
* `TITLE_ONLY` - Title only (no content)
* `BLANK` - Blank slide with title and subtitle
* `CONTENT_WITH_CAPTION` - Content + explanatory points

**IMPORTANT:** You MUST use these exact layout names. Do not create variations like "BLEND", "MIXED", "CUSTOM", or any other layout name not listed above.

---

## **Content Preservation Guidelines:**

- **EXTRACT, DON'T CREATE**: Pull text directly from the provided content
- **PRESERVE ORIGINAL WORDING**: Use the exact phrases and terminology from the source
- **MAINTAIN FACTUAL ACCURACY**: Don't add information not present in the original content
- **ORGANIZE LOGICALLY**: Structure the existing content into appropriate slide layouts
- **USE EXISTING HEADINGS**: Extract section titles and headings directly from the content
- **KEEP ORIGINAL DETAILS**: Include specific data, numbers, and examples as provided

---

## **Layout Usage Guidelines:**

* **TITLE**: Use for the opening slide of your presentation
* **TITLE_AND_CONTENT**: Use for slides with a list of related points or bullet items
* **SECTION_HEADER**: Use to introduce new sections or major topic transitions
* **TWO_CONTENT**: Use when you have two distinct but related sets of information
* **COMPARISON**: Use specifically for comparing two things side-by-side with clear labels
* **TITLE_ONLY**: Use for transition slides or emphasis slides with just a title
* **BLANK**: Use for slides that need visual content or diagrams (title + subtitle only)
* **CONTENT_WITH_CAPTION**: Use for explanatory content that needs detailed context

---

## **Guidelines:**

* Start with a `TITLE` layout for the opening slide
* Use a **mix** of slide types for visual and informational diversity
* Ensure bullet points are informative and presentation-ready
* Use `CONTENT_WITH_CAPTION` layout where a visual explanation or long paragraph would be appropriate
* Use `SECTION_HEADER` or `TITLE_ONLY` to break content flow or introduce a new segment
* Each content slide should have **4–6 detailed bullet points**
* Avoid repeating slide types too often
* Organize content logically and clearly

---

## **JSON Output Requirements**

1. **Return ONLY valid JSON** - no markdown formatting, no backticks, no explanatory text
2. **Use only the 8 layout types listed above** - do not invent new layouts
3. **Each slide object must have the exact field names** shown in the schema
4. **All strings must be properly quoted**
5. **Arrays must contain strings only**

---

## **Schema Definition**

```json
{
  "title": "string",
  "presentation_content": [
    // Array of slide objects, each with one of these exact structures:

    // TITLE slide
    {
      "layout": "TITLE",
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

    // BLANK slide
    {
      "layout": "BLANK",
      "title": "string",
      "subtitle": "string"
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
---
**Content Processing Instructions:**

1. Read through the entire provided content first
2. Identify natural sections, headings, and divisions
3. Extract titles and headings exactly as written
4. Copy bullet points, lists, and paragraphs verbatim
5. Organize into slides following the logical flow of the original content
6. Choose layouts that best fit how the content is naturally structured
7. Don't split content unnecessarily - keep related information together
8. Maintain the original sequence and order of information
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

## **Example Outputs**

### **Example 1: "Climate Change Solutions" (Research/Environmental Topic)**

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
      "points": ["Global warming accelerates ice melt, rising sea levels, and extreme weather", "Annual global temperatures continue to break historical records", "Widespread environmental and economic impacts already visible across continents"]
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

### **Example 2: "Digital Marketing Strategy" (Business Topic)**

```json
{
  "title": "Digital Marketing Strategy 2025",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "Digital Marketing Strategy 2025"
    },
    {
      "layout": "SECTION_HEADER",
      "title": "Market Analysis",
      "subtitle": "Understanding today's digital landscape"
    },
    {
      "layout": "TWO_CONTENT",
      "title": "Current Challenges and Opportunities",
      "left_points": [
        "Ad-blocking software reduces traditional display effectiveness",
        "Privacy regulations limit data collection capabilities",
        "Increasing competition for customer attention",
        "Rising costs of paid advertising platforms"
      ],
      "right_points": [
        "AI-powered personalization creates deeper engagement",
        "Video content consumption continues exponential growth",
        "Social commerce integration streamlines purchase journeys",
        "Influencer partnerships provide authentic brand connections"
      ]
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Core Strategy Pillars",
      "points": [
        "Content-first approach with storytelling at the center",
        "Multi-channel attribution for comprehensive campaign tracking",
        "Customer lifecycle automation from awareness to retention",
        "Data-driven decision making with real-time optimization",
        "Community building through authentic brand experiences"
      ]
    },
    {
      "layout": "BLANK",
      "title": "Implementation Timeline",
      "subtitle": "Q1-Q4 2025 roadmap visualization"
    },
    {
      "layout": "COMPARISON",
      "title": "Budget Allocation Strategy",
      "left_heading": "Traditional Channels",
      "right_heading": "Emerging Channels",
      "left_points": [
        "Search engine marketing (35%)",
        "Social media advertising (25%)",
        "Email marketing campaigns (15%)",
        "Display and retargeting (10%)"
      ],
      "right_points": [
        "Influencer partnerships (8%)",
        "Podcast advertising (4%)",
        "Connected TV campaigns (2%)",
        "Experimental channels (1%)"
      ]
    }
  ]
}
```

### **Example 3: "Ancient Rome History" (Educational Topic)**

```json
{
  "title": "The Rise and Fall of Ancient Rome",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "The Rise and Fall of Ancient Rome"
    },
    {
      "layout": "TITLE_ONLY",
      "title": "From Kingdom to Empire: 753 BC - 476 AD"
    },
    {
      "layout": "COMPARISON",
      "title": "Roman Republic vs Roman Empire",
      "left_heading": "Republic (509-27 BC)",
      "right_heading": "Empire (27 BC-476 AD)",
      "left_points": [
        "Senate-controlled governance system",
        "Consul leadership with term limits",
        "Expansion through military conquest",
        "Citizen participation in politics"
      ],
      "right_points": [
        "Emperor as supreme authority",
        "Bureaucratic administrative structure",
        "Focus on consolidation and defense",
        "Professional standing armies"
      ]
    },
    {
      "layout": "CONTENT_WITH_CAPTION",
      "title": "Roman Engineering Marvels",
      "points": [
        "Aqueduct systems transported fresh water across hundreds of miles to major cities",
        "The Pantheon's concrete dome remained the world's largest for over 1,000 years",
        "Roman road network totaled over 250,000 miles, connecting the entire Mediterranean world",
        "Advanced siege warfare technology enabled conquest of heavily fortified cities"
      ]
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Factors in Rome's Decline",
      "points": [
        "Economic inflation weakened currency and trade systems",
        "Barbarian invasions pressured frontier defenses",
        "Political instability with frequent emperor changes",
        "Rise of Christianity altered traditional Roman values",
        "Administrative challenges of governing vast territories"
      ]
    },
    {
      "layout": "SECTION_HEADER",
      "title": "Legacy and Impact",
      "subtitle": "How Rome shaped Western civilization"
    }
  ]
}
```

### **Example 4: "Artificial Intelligence Ethics" (Technology/Philosophy Topic)**

```json
{
  "title": "AI Ethics: Navigating the Future of Intelligent Systems",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "AI Ethics: Navigating the Future of Intelligent Systems"
    },
    {
      "layout": "BLANK",
      "title": "The Ethical Imperative",
      "subtitle": "Why AI ethics matter more than ever"
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Core Ethical Principles in AI Development",
      "points": [
        "Fairness and non-discrimination in algorithmic decision-making",
        "Transparency and explainability of AI system operations",
        "Privacy protection and data governance standards",
        "Human oversight and meaningful control over AI systems",
        "Accountability and responsibility for AI-driven outcomes"
      ]
    },
    {
      "layout": "TWO_CONTENT",
      "title": "Stakeholder Perspectives",
      "left_points": [
        "Developers need clear ethical guidelines for implementation",
        "Regulators require enforceable standards and compliance frameworks",
        "Companies seek competitive advantage while managing risks",
        "Researchers push boundaries while considering societal impact"
      ],
      "right_points": [
        "Users demand transparency about how AI affects their lives",
        "Communities need protection from algorithmic bias and harm",
        "Workers require support during AI-driven job transitions",
        "Society expects benefits to be distributed equitably"
      ]
    },
    {
      "layout": "CONTENT_WITH_CAPTION",
      "title": "Real-World Case Studies",
      "points": [
        "Facial recognition systems in law enforcement raise concerns about privacy and racial bias",
        "AI hiring tools have been found to discriminate against women and minorities",
        "Autonomous vehicles must make split-second ethical decisions in emergency situations",
        "Healthcare AI systems can perpetuate existing disparities in medical treatment"
      ]
    },
    {
      "layout": "TITLE_ONLY",
      "title": "Building an Ethical AI Future Together"
    }
  ]
}
```

### **Example 5: "Personal Finance Basics" (Practical/Educational Topic)**

```json
{
  "title": "Personal Finance Fundamentals",
  "presentation_content": [
    {
      "layout": "TITLE",
      "title": "Personal Finance Fundamentals"
    },
    {
      "layout": "COMPARISON",
      "title": "Assets vs Liabilities",
      "left_heading": "Assets (What You Own)",
      "right_heading": "Liabilities (What You Owe)",
      "left_points": [
        "Savings and checking accounts",
        "Investment portfolios and retirement funds",
        "Real estate and property ownership",
        "Valuable personal possessions"
      ],
      "right_points": [
        "Credit card debt and personal loans",
        "Mortgage and home equity loans",
        "Student loans and educational debt",
        "Auto loans and financing agreements"
      ]
    },
    {
      "layout": "CONTENT_WITH_CAPTION",
      "title": "The 50/30/20 Budgeting Rule",
      "points": [
        "50% of after-tax income goes to essential needs like housing, utilities, groceries, and minimum debt payments",
        "30% allocated to wants and lifestyle choices such as dining out, entertainment, hobbies, and non-essential shopping",
        "20% dedicated to savings and debt repayment above minimums, including emergency funds and retirement contributions"
      ]
    },
    {
      "layout": "SECTION_HEADER",
      "title": "Investment Strategies",
      "subtitle": "Building wealth over time"
    },
    {
      "layout": "TWO_CONTENT",
      "title": "Investment Options by Risk Level",
      "left_points": [
        "High-yield savings accounts offer safety with modest returns",
        "Government bonds provide stable income with low risk",
        "Index funds deliver market returns with diversification",
        "Target-date funds automatically adjust risk over time"
      ],
      "right_points": [
        "Individual stocks can provide high returns but carry significant risk",
        "Real estate investment trusts (REITs) offer property exposure",
        "Cryptocurrency represents emerging digital asset class",
        "Options and derivatives require advanced knowledge and carry high risk"
      ]
    },
    {
      "layout": "TITLE_AND_CONTENT",
      "title": "Action Steps for Financial Success",
      "points": [
        "Create and stick to a monthly budget tracking all income and expenses",
        "Build an emergency fund covering 3-6 months of living expenses",
        "Pay off high-interest debt starting with credit cards first",
        "Maximize employer 401(k) matching contributions for free money",
        "Regularly review and adjust your financial plan as life changes"
      ]
    }
  ]
}
```

---

These examples demonstrate various structural approaches:
- **Example 1**: Starts with problem, moves through solutions, ends with action items
- **Example 2**: Opens with analysis, focuses on strategy, concludes with implementation
- **Example 3**: Uses chronological flow with comparative analysis
- **Example 4**: Begins conceptually, examines multiple perspectives, grounds in reality
- **Example 5**: Starts with fundamentals, progresses to advanced concepts, ends with actionable steps

Notice how different slide types appear in various positions, showing flexibility in presentation flow and structure.
---

## **Final Reminders**

- **NEVER** use layout names other than the 8 specified above
- **ALWAYS** include all required fields for each layout type
- **ENSURE** your JSON is valid and properly formatted
- **MATCH** the content structure to the appropriate layout type
- **START** with a TITLE slide and use a mix of layout types throughout
