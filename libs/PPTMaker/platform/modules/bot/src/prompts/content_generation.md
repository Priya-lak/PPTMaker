### **Prompt Instruction (Refactored)**

You will be given a **topic**. Based on that topic, generate a structured presentation outline in **JSON format** with the following structure:

### **Output Format Example**

(For topic: *Artificial Intelligence*)

```json
{
  "title_page": {
    "type": "first_page",
    "title": "Introduction to Artificial Intelligence",
    "description": "Understanding the basics and real-world applications of AI"
  },
  "presentation_content": [
    {
      "type": "content_page",
      "title": "What is Artificial Intelligence?",
      "bullet_points": [
        "Simulation of human intelligence in machines",
        "Includes learning, reasoning, and self-correction",
        "Enables machines to perform tasks that typically require human intelligence"
      ]
    },
    {
      "type": "image_page",
      "title": "Types of AI",
      "image_description": "Diagram showing three levels of AI: Narrow AI (current), General AI (theoretical), and Superintelligent AI (future concept)",
      "caption": "AI exists on a spectrum from specialized narrow AI we use today to theoretical superintelligent systems",
      "layout": "side_by_side"
    },
    {
      "type": "content_page",
      "title": "Applications of AI",
      "bullet_points": [
        "Healthcare: Diagnosis, drug discovery, personalized medicine",
        "Finance: Fraud detection, algorithmic trading",
        "Customer Service: Chatbots, virtual assistants",
        "Transportation: Self-driving cars, traffic prediction"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Future of AI",
      "image_description": "Timeline visualization showing AI evolution from current applications to future developments with ethical considerations",
      "caption": "The next decade will see AI integration across all industries while addressing safety and ethical challenges",
      "layout": "image_bottom"
    }
  ]
}
```

### **Page Types and Requirements:**

#### **Title Page (Required)**
- `type`: `"first_page"`
- `title`: Main presentation title
- `description`: Brief overview of the presentation

#### **Content Pages**
- `type`: `"content_page"` or `"title_page"`
- `title`: Slide title
- `bullet_points`: List of 3–5 bullet points (can be `null`)

#### **Image Pages**
- `type`: `"image_page"` or `"image_content_page"`
- `title`: Slide title
- `image_description`: Detailed description of the visual content
- `caption`: Long explanatory text about the image
- `layout`: Choose from `"side_by_side"`, `"image_bottom"`, `"image_title_caption"`, or `"standard"`

### **Guidelines:**
- Keep total slides between **4–6** (excluding title page)
- Mix content and image pages for visual variety
- Use image pages for concepts that benefit from visual representation
- Choose appropriate layouts based on content type
- Keep content concise and presentation-ready

**IMPORTANT**: Output only the JSON structure without any explanatory text, markdown formatting, or code blocks.
