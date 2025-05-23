import requests
from duckduckgo_search import DDGS

from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("ImageGeneratorService", is_request=False)

logger, listener = log.get_logger()

listener.start()


class ImageSearchService:
    def __init__(self):
        self.service = DDGS()

    def search_by_topic(self, topic, image_path="static/images/filename.jpg"):
        logger.info(f"Searching for the topic {topic}")
        image_result = self.service.images(topic, max_results=2)
        logger.info(f"Extracted 2 results {image_result}")
        self._download_image(image_url=image_result[1]["image"], image_path=image_path)

    def _download_image(self, image_url, image_path):
        try:
            logger.info(f"requesting {image_url}")
            response = requests.get(image_url)
            logger.info(f"Response {response}")
            if response.status_code == 200:
                with open(image_path, "wb") as file:
                    file.write(response.content)
                logger.info(f"Image saved to {image_path}")
            else:
                logger.error(
                    f"Failed to download image. Status code: {response.status_code}"
                )
        except Exception as e:
            logger.error(f"Error occurred: {e}")


def main():
    service = ImageSearchService()

    service.search_by_topic("fruits basket anime")


if __name__ == "__main__":
    main()
