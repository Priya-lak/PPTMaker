import json
import traceback

from libs.PPTMaker.enums.themes_styles_enum import StylesEnum, ThemesEnum
from libs.PPTMaker.platform.modules.bot.src.constants import LAYOUT_GENERATION_PROMPT
from libs.PPTMaker.platform.modules.bot.src.models.custom_layout_model import (
    SlideLayoutParams,
)
from libs.PPTMaker.platform.modules.bot.src.models.slide_layout_models import (
    PresentationModel,
)
from libs.PPTMaker.platform.modules.bot.src.services.image_search_service import (
    ImageSearchService,
)
from libs.PPTMaker.platform.modules.bot.src.services.llm_service import LLMService
from libs.PPTMaker.platform.modules.bot.src.services.ppt_maker_service import (
    PPTXGenerator,
)
from libs.PPTMaker.platform.modules.bot.src.utils.prompt_formatter_util import (
    params_to_prompt_string,
)
from libs.PPTMaker.platform.modules.bot.src.utils.styles import StyleFactory
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("PPTGeneratorService", is_request=False)

logger, listener = log.get_logger()

listener.start()


class PPTGenerator:
    def __init__(self, style: StylesEnum, theme: ThemesEnum = None):
        self.llm_service = LLMService()
        self.style = StyleFactory.create_style(style)
        self.ppt_service = PPTXGenerator(style=self.style, theme=theme.template_path)
        self.image_search_service = ImageSearchService()

    def generate_presentation_layout(
        self, content: str, custom_params: SlideLayoutParams = None
    ):
        if custom_params:
            formatted_custom_params = params_to_prompt_string(custom_params)
            logger.info(f"custom params {formatted_custom_params}")
        messages = [
            {"role": "system", "content": LAYOUT_GENERATION_PROMPT},
            {
                "role": "system",
                "content": f"Use the following as the main content to generate the response:: {content}",
            },
        ]
        logger.info("Calling LLM")
        response = self.llm_service.call_llm(
            messages, response_format={"type": "json_object"}
        )
        response = PresentationModel(**json.loads(response))

        return response

    def _save_presentation(self, title):
        try:
            logger.info("Saving presentation to file")
            output_file = f"temp/{title}.pptx".replace(" ", "-")
            self.ppt_service.save_presentation(output_file)
            logger.info(f"Presentation saved to {output_file}")
            return output_file
        except Exception as e:
            logger.error(f"An error occurred while saving presentation {str(e)}")
            raise e

    def create_presentation_from_layout(self, layout: PresentationModel) -> str:
        logger.info("Creating presentation from content")
        try:
            title = layout.title
            for content_slides in layout.presentation_content:
                logger.info(f"Content: {content_slides}")
                self.ppt_service.layout_manager.create_slide(
                    **content_slides.model_dump()
                )
            output_file = self._save_presentation(title=title)
            return output_file
        except Exception as e:
            logger.error(
                f"An error occurred while creating presentation {traceback.print_exc()}"
            )
            return None


def main():
    style = StylesEnum.DARK
    service = PPTGenerator(
        style=style.value, theme="static/templates/madison-lilac.pptx"
    )
    content = "**section 1:** **Introduction to AI in Healthcare**\nArtificial intelligence (AI) represents a crucial component in the transformation of healthcare. Its application in medical research, diagnosis, treatment planning, and patient care has improved patient outcomes, reduced healthcare costs, and enhanced the efficiency of clinical workflows. As the complexity of healthcare datasets increases, AI's ability to analyze and learn from vast amounts of data makes it an indispensable tool in modern healthcare.\n\n**section 2:** **Applications of AI in Healthcare Research**\n- **Genomic Analysis**: AI algorithms enable researchers to efficiently analyze genomic data, identify patterns associated with genetic diseases, and discover new treatments.\n- **Clinical Trial Predictions**: AI models predict patient responses to treatments, improving clinical trial success rates and reducing trial participant risks.\n- **Disease Modeling**: AI simulations model disease progression, facilitating the development of early intervention strategies and personalized treatment plans.\n- **Literature Reviews**: AI-assisted literature reviews expedite the search for relevant studies, saving time and enhancing the accuracy of systematic reviews.\n\n**section 3:** **AI in Healthcare Diagnostics**\n- **Image Analysis**: AI algorithms enhance the accuracy of medical imaging analysis, allowing for more precise diagnoses, such as cancer detection and cardiac conditions.\n- **Clinical Decision Support Systems**: AI-powered systems provide physicians with data-driven recommendations for diagnosis and treatment, reducing errors and improving patient care.\n- **Predictive Analytics**: AI predictive models identify high-risk patients, enabling proactive interventions and reducing the likelihood of adverse events.\n- **Natural Language Processing (NLP)**: AI-based NLP systems analyze patient symptoms, medical histories, and treatment plans, streamlining diagnosis and improving the accuracy of diagnosis.\n\n**section 4:** **AI in Healthcare Treatment Planning**\n- **Personalized Medicine**: AI models create individualized treatment plans based on a patient's unique genetic profile, medical history, and treatment response.\n- **Medication Adherence**: AI systems monitor patient medication adherence and alert healthcare providers to potential non-adherence, ensuring timely interventions and improving patient compliance.\n- **Rehabilitation Plans**: AI-based analysis creates tailored rehabilitation plans, improving patient recovery outcomes and reducing healthcare costs.\n- **Treatment Outcome Prediction**: AI models predict treatment outcomes, helping healthcare providers make data-driven decisions about treatment plans and patient care pathways.\n\n**section 5:** **Challenges and Limitations in AI in Healthcare**\n- **Data Quality and Standardization**: High-quality data is essential for AI model training. However, existing healthcare data is often fragmented, inconsistent, and difficult to integrate.\n- **Bias and Discrimination**: AI models can perpetuate existing biases if trained on biased data, leading to unfair treatment and adverse health outcomes.\n- **Regulatory Frameworks**: Clarity on regulatory requirements for AI in healthcare development, deployment, and maintenance is essential for ensuring patient safety and provider accountability.\n- **Human-AI Collaboration**: Successful AI implementation in healthcare requires effective collaboration between human healthcare providers and AI systems, enhancing patient care and improving healthcare outcomes.\n\n**section 6:** **Future Directions of AI in Healthcare**\nAs AI continues to revolutionize healthcare, future directions include:\n\n- **Integration with Wearable Devices and IoT**: Seamless data transfer and real-time analytics between AI systems and wearable devices and IoT sensors enhance patient monitoring and predictive healthcare.\n- **Explainable AI (XAI)**: Developing AI that provides transparent and interpretable insights into its decision-making processes increases trust in AI and enhances patient care.\n- **Federated Learning**: AI systems that can learn from decentralized data sources without requiring data transfer will enable more efficient and patient-centric healthcare research and treatment development.\n- **AI-Powered Mental Health Support**: AI-based chatbots and mental health platforms offer accessible, patient-friendly mental health support, reducing healthcare disparities and improving mental wellbeing.\n\nIn conclusion, AI has the potential to profoundly impact every aspect of healthcare, from research and diagnostics to treatment planning and patient support. With ongoing advancements in AI technologies and a comprehensive understanding of its potential and limitations, the future of healthcare will be increasingly shaped by the interaction of humans and artificial intelligence."
    layout = service.generate_presentation_layout(content)
    service.create_presentation_from_layout(layout=layout)


if __name__ == "__main__":
    main()
