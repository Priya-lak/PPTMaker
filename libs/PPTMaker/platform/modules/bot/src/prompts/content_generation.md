## **Instructions**

You will be given a **topic**. Based on that topic, generate a structured presentation outline in **JSON format** with the following structure:



## **Page Types and Requirements:**

### **Title Page (Required)**
- `type`: `"first_page"`
- `title`: Main presentation title
- `description`: Brief overview of the presentation

### **Content Pages**
- `type`: `"content_page"` or `"title_page"`
- `title`: Slide title
- `points`: List of 5-6 bullet points (can be `null`)

### **Image Pages**
- `type`: `"image_page"` or `"image_content_page"`
- `title`: Slide title
- `image_description`: Detailed description of the visual content
- `caption`: Long explanatory text about the image
- `layout`: Choose from `"side_by_side"`, `"image_bottom"`, `"image_title_caption"`, or `"standard"`

## **Guidelines:**
- Keep total slides between **4–6** (excluding title page)
- Mix content and image pages for visual variety
- Make the bullet points more descriptive
- Use image pages for concepts that benefit from visual representation
- Choose appropriate layouts based on content type
- Keep content concise and presentation-ready
- Play around with the layouts and positions of slides, don't necessarily copy the example




## **Output Format Example**

### Example 1: Climate Change Solutions

```json
{
  "title_page": {
    "type": "first_page",
    "title": "Climate Change: Solutions for a Sustainable Future",
    "description": "Exploring innovative approaches to combat global warming and build environmental resilience"
  },
  "presentation_content": [
    {
      "type": "image_content_page",
      "title": "The Climate Crisis Reality",
      "image_search_keyword": "global warming effects rising sea levels",
      "image_description": "Split-screen comparison showing Arctic ice sheets melting, flooded coastal cities, and extreme weather events including hurricanes and droughts",
      "caption": "Climate change impacts are accelerating globally, with sea levels rising 3.3mm annually and extreme weather events increasing by 70% since 2000",
      "layout": "image_title_caption"
    },
    {
      "type": "content_page",
      "title": "Renewable Energy Revolution",
      "points": [
        "Solar power costs have dropped 90% in the last decade, making it the cheapest electricity source in most regions",
        "Wind energy now generates enough electricity to power 130 million American homes annually",
        "Battery storage technology improvements enable 24/7 renewable energy availability even when sun and wind aren't present",
        "Green hydrogen production offers clean fuel alternatives for heavy industry and long-distance transportation",
        "Smart grid systems optimize energy distribution and reduce waste by up to 15% through AI-powered management"
      ]
    },
    {
      "type": "image_page",
      "title": "Carbon Capture Technologies",
      "image_search_keyword": "direct air capture carbon removal technology",
      "image_description": "Industrial facility with large fan systems pulling CO2 from atmosphere, underground storage caverns, and forest restoration projects showing natural carbon sequestration",
      "caption": "Direct air capture facilities can remove 1 million tons of CO2 annually, while reforestation efforts sequester 2.6 billion tons globally each year",
      "layout": "side_by_side"
    },
    {
      "type": "content_page",
      "title": "Individual Action Impact",
      "points": [
        "Transportation changes like electric vehicles and public transit can reduce personal carbon footprint by 2.3 tons CO2 annually",
        "Home energy efficiency improvements through insulation and smart thermostats cut emissions by 15-30% per household",
        "Dietary shifts toward plant-based meals just twice weekly saves equivalent of 1,200 miles of driving emissions",
        "Supporting businesses with verified carbon-neutral practices amplifies individual impact through market demand",
        "Community solar programs allow renters and homeowners to access clean energy without rooftop installations"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Global Policy Success Stories",
      "image_search_keyword": "renewable energy policy success Denmark Costa Rica",
      "image_description": "World map highlighting countries with successful green policies: Denmark's wind farms, Costa Rica's hydroelectric systems, and Norway's electric vehicle adoption rates",
      "caption": "Denmark generates 140% of its electricity needs from wind power, while Costa Rica runs on 99% renewable energy and Norway leads with 80% electric vehicle market share",
      "layout": "image_bottom"
    }
  ]
}
```

### Example 2: Space Exploration

```json
{
  "title_page": {
    "type": "first_page",
    "title": "The New Space Age: Humanity's Next Frontier",
    "description": "Examining current achievements and future possibilities in space exploration and colonization"
  },
  "presentation_content": [
    {
      "type": "content_page",
      "title": "Commercial Space Revolution",
      "points": [
        "SpaceX has reduced launch costs from $10,000 to $1,400 per kilogram through reusable rocket technology",
        "Private companies now handle 60% of all satellite deployments, democratizing access to space-based services",
        "Space tourism industry projected to reach $8 billion by 2030 with companies offering suborbital and orbital flights",
        "Asteroid mining ventures are developing technology to extract rare earth metals worth trillions of dollars",
        "Manufacturing in zero gravity enables production of fiber optics and pharmaceuticals impossible to create on Earth"
      ]
    },
    {
      "type": "image_page",
      "title": "Mars Mission Architecture",
      "image_search_keyword": "Mars colonization habitat spacecraft landing",
      "image_description": "Detailed cross-section of Mars habitat modules with life support systems, greenhouse domes, solar arrays, and landing craft on the Martian surface with red rocky landscape",
      "caption": "Mars missions require integrated systems including pressurized habitats, closed-loop life support, in-situ resource utilization, and reliable communication with Earth across 225 million kilometers",
      "layout": "standard"
    },
    {
      "type": "image_content_page",
      "title": "Scientific Discoveries Beyond Earth",
      "image_search_keyword": "James Webb telescope exoplanet discovery",
      "image_description": "Composite image showing James Webb Space Telescope's infrared view of distant galaxies, artist rendering of potentially habitable exoplanets, and molecular signatures indicating water vapor",
      "caption": "The James Webb Space Telescope has identified over 5,000 exoplanets, with 50+ located in habitable zones where liquid water could exist",
      "layout": "side_by_side"
    },
    {
      "type": "content_page",
      "title": "International Space Collaboration",
      "points": [
        "International Space Station represents 15-nation partnership conducting over 3,000 scientific experiments since 2000",
        "Artemis Accords unite 28 countries in peaceful lunar exploration principles and resource sharing agreements",
        "European Space Agency's Copernicus program provides free Earth observation data to 150,000+ users globally for climate monitoring",
        "China-Russia lunar base partnership plans permanent human presence on Moon's south pole by 2035",
        "Global space debris tracking networks share data to protect $400 billion worth of active satellites from collision"
      ]
    }
  ]
}
```

### Example 3: Mental Health Awareness

```json
{
  "title_page": {
    "type": "first_page",
    "title": "Breaking the Silence: Mental Health in the Modern World",
    "description": "Understanding, supporting, and improving mental wellness in our communities and workplaces"
  },
  "presentation_content": [
    {
      "type": "image_content_page",
      "title": "The Hidden Statistics",
      "image_search_keyword": "mental health statistics depression anxiety infographic",
      "image_description": "Data visualization showing mental health statistics with human silhouettes, percentage breakdowns of anxiety (18.1%), depression (8.5%), and workplace stress factors affecting different age groups",
      "caption": "One in four people worldwide will experience mental health challenges, yet 60% never seek professional help due to stigma and accessibility barriers",
      "layout": "image_title_caption"
    },
    {
      "type": "content_page",
      "title": "Workplace Mental Health Crisis",
      "points": [
        "Employee burnout affects 76% of workers, costing companies $125-190 billion annually in healthcare expenses",
        "Remote work isolation has increased anxiety and depression rates by 25% since 2020, particularly among younger employees",
        "Only 23% of organizations provide comprehensive mental health benefits despite proven ROI of $4 return per $1 invested",
        "Psychological safety in teams correlates with 27% lower turnover and 12% increase in productivity metrics",
        "Flexible work arrangements and mental health days reduce stress-related absences by up to 40% in participating companies"
      ]
    },
    {
      "type": "image_page",
      "title": "Technology-Enabled Support",
      "image_search_keyword": "mental health apps therapy technology telehealth",
      "image_description": "Split view showing person using mental health app on smartphone, virtual therapy session on laptop, and AI chatbot interface providing 24/7 crisis support",
      "caption": "Digital mental health platforms serve 100+ million users globally, providing accessible therapy, meditation, and crisis intervention with 24/7 availability",
      "layout": "image_bottom"
    },
    {
      "type": "content_page",
      "title": "Building Supportive Communities",
      "points": [
        "Peer support groups reduce hospitalization rates by 40% and improve long-term recovery outcomes for individuals with severe mental illness",
        "Schools implementing social-emotional learning programs see 23% improvement in academic performance and reduced behavioral problems",
        "Community mental health first aid training enables non-professionals to recognize crisis signs and provide initial support before professional help arrives",
        "Faith-based and cultural organizations serve as crucial access points for mental health resources in underserved communities",
        "Workplace employee resource groups focused on mental health create safe spaces for sharing experiences and reducing stigma among colleagues"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Prevention and Early Intervention",
      "image_search_keyword": "mental health prevention exercise meditation social connection",
      "image_description": "Collage showing various prevention activities: group exercise class, meditation session, family dinner, community volunteering, and person journaling in nature",
      "caption": "Prevention strategies including regular exercise, social connections, mindfulness practices, and community engagement can reduce mental health crisis risk by up to 50%",
      "layout": "standard"
    }
  ]
}
```

### Example 4: Sustainable Agriculture

```json
{
  "title_page": {
    "type": "first_page",
    "title": "Feeding the Future: Sustainable Agriculture Revolution",
    "description": "Innovative farming methods that nourish people while protecting our planet's resources"
  },
  "presentation_content": [
    {
      "type": "content_page",
      "title": "The Agriculture Challenge",
      "points": [
        "Global population will reach 9.7 billion by 2050, requiring 70% increase in food production on existing farmland",
        "Climate change threatens crop yields with extreme weather reducing harvests by 10-25% in major growing regions",
        "Industrial farming consumes 70% of freshwater globally while degrading soil at rates 10-40 times faster than regeneration",
        "Agricultural runoff creates 400+ ocean dead zones, destroying marine ecosystems and fisheries worldwide",
        "Smallholder farmers producing 80% of world's food face increasing economic pressure from industrial agriculture consolidation"
      ]
    },
    {
      "type": "image_page",
      "title": "Vertical Farming Innovation",
      "image_search_keyword": "vertical farming LED hydroponics urban agriculture",
      "image_description": "Multi-story indoor farm facility with LED-lit growing towers, robotic harvesting systems, and precise nutrient delivery systems growing leafy greens and herbs",
      "caption": "Vertical farms use 95% less water and 99% less land while producing 365 harvests per year in controlled environments, yielding 390 times more per square foot than traditional farming",
      "layout": "side_by_side"
    },
    {
      "type": "image_content_page",
      "title": "Regenerative Farming Practices",
      "image_search_keyword": "cover crops soil health regenerative agriculture carbon sequestration",
      "image_description": "Side-by-side comparison of degraded farmland versus regenerative farm showing diverse cover crops, healthy soil cross-section with earthworms, and livestock integrated with crop rotation",
      "caption": "Regenerative agriculture sequesters 1.85 tons of carbon per acre annually while improving soil health, increasing biodiversity, and boosting farm profitability by 15-25%",
      "layout": "image_bottom"
    },
    {
      "type": "content_page",
      "title": "Precision Agriculture Technology",
      "points": [
        "GPS-guided tractors and drones reduce pesticide use by 15-20% through targeted application only where needed",
        "Soil sensors monitor moisture, nutrients, and pH levels in real-time, optimizing irrigation and fertilizer timing for maximum efficiency",
        "Satellite imagery and AI algorithms predict crop diseases and pest infestations 2-3 weeks before visible symptoms appear",
        "Variable rate seeding technology adjusts planting density based on soil conditions, improving yields by 8-15% per field",
        "Blockchain technology enables farm-to-table traceability, reducing food fraud and enabling premium pricing for sustainable practices"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Alternative Protein Sources",
      "image_search_keyword": "insect farming lab grown meat plant protein alternatives",
      "image_description": "Laboratory showing cultured meat production, cricket farming facilities, and plant-based protein processing equipment alongside nutritional comparison charts",
      "caption": "Alternative proteins require 96% less land, 87% less water, and produce 89% fewer emissions than conventional livestock while meeting growing global protein demand",
      "layout": "standard"
    }
  ]
}
```

### Example 5: Digital Privacy & Security

```json
{
  "title_page": {
    "type": "first_page",
    "title": "Digital Privacy in the Connected Age",
    "description": "Protecting personal information and maintaining security in an increasingly digital world"
  },
  "presentation_content": [
    {
      "type": "image_page",
      "title": "The Data Collection Reality",
      "image_search_keyword": "data collection personal information tracking cookies surveillance",
      "image_description": "Visualization of person surrounded by digital data streams from smartphone, laptop, smart home devices, and social media platforms, with data flowing to corporate servers",
      "caption": "Average person generates 2.5 quintillion bytes of data daily through 40+ connected devices, with tech companies collecting over 1,500 data points per individual",
      "layout": "image_title_caption"
    },
    {
      "type": "content_page",
      "title": "Common Privacy Threats",
      "points": [
        "Social media platforms track users across 70% of top websites through embedded pixels and tracking cookies, even when logged out",
        "Smart home devices like voice assistants record conversations 24/7, storing audio data for up to 7 years in some cases",
        "Location tracking through smartphones creates detailed movement patterns used for targeted advertising and sold to data brokers",
        "Public Wi-Fi networks expose unencrypted data to potential interception, with 87% of users connecting without VPN protection",
        "Data breaches affect 1 in 3 Americans annually, exposing social security numbers, financial information, and personal communications to criminals"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Cybersecurity Defense Layers",
      "image_search_keyword": "cybersecurity multi-factor authentication encryption firewall",
      "image_description": "Layered security diagram showing firewall protection, encrypted connections, multi-factor authentication, and secure password management protecting user data and devices",
      "caption": "Multi-layered security approaches reduce successful cyber attacks by 99.9% when combining strong passwords, encryption, regular updates, and user education",
      "layout": "side_by_side"
    },
    {
      "type": "content_page",
      "title": "Privacy Protection Strategies",
      "points": [
        "Use privacy-focused browsers like Firefox with strict tracking protection enabled, reducing data collection by 85% compared to default settings",
        "Enable two-factor authentication on all accounts, which prevents 99.9% of automated attacks even with compromised passwords",
        "Regular privacy audits of social media accounts and app permissions help identify and revoke unnecessary data access permissions",
        "VPN services encrypt internet traffic and mask location data, essential for protecting sensitive communications on public networks",
        "Privacy-focused alternatives to mainstream services exist for search engines, email, messaging, and cloud storage with end-to-end encryption"
      ]
    },
    {
      "type": "image_content_page",
      "title": "Legislative Privacy Landscape",
      "image_search_keyword": "GDPR privacy laws data protection regulations global",
      "image_description": "World map showing privacy legislation coverage: GDPR in Europe, CCPA in California, similar laws spreading globally with enforcement statistics and user rights icons",
      "caption": "Privacy regulations now protect 1.8 billion people globally, with companies facing up to 4% of annual revenue in fines for violations, driving improved data handling practices",
      "layout": "image_bottom"
    }
  ]
}
```

## **IMPORTANT**:
 Output only the JSON structure without any explanatory text, markdown formatting, or code blocks.
