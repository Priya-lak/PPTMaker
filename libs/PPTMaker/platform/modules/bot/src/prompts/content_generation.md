

###  **Prompt Instruction (Refactored)**

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
      "type": "content_page",
      "title": "Types of AI",
      "bullet_points": [
        "Narrow AI: Specialized for a specific task (e.g., Siri, Google Maps)",
        "General AI: Can perform any intellectual task a human can do (still theoretical)",
        "Superintelligent AI: Surpasses human intelligence (a future concept)"
      ]
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
      "type": "content_page",
      "title": "Future of AI",
      "bullet_points": [
        "Ethical concerns and regulation",
        "Increased human-machine collaboration",
        "AI in creative fields like art, music, and writing",
        "Continued research on safe and explainable AI"
      ]
    }
  ]
}

```

### Notes:

* The first object must be of type `"first_page"` and contain a title and description.
* Subsequent slides must be of type `"content_page"` with:

  * A `title`
  * A list of 3–5 `bullet_points`
* Keep the total number of slides between **4–6**
* Keep it concise, informative, and suitable for a basic presentation.

**IMPORTANT**: Do not include any explanatory text, markdown formatting, or code blocks.


