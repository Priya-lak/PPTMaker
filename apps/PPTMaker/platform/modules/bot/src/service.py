import os

from fastapi.responses import FileResponse

from apps.PPTMaker.platform.modules.bot.src.dto import (
    ContentGenerationRequest,
    DownloadFileRequest,
    PresentationGenerationRequest,
)
from libs.PPTMaker.enums.themes_styles_enum import StylesEnum
from libs.PPTMaker.platform.modules.bot.src.services.content_generation_service import (
    ContentGenerationService,
)
from libs.PPTMaker.platform.modules.bot.src.services.ppt_generator_service import (
    PPTGenerator,
)


def create_customized_presentation(request_data: PresentationGenerationRequest):
    service = PPTGenerator(style=request_data.style, theme=request_data.theme)
    layout = service.generate_presentation_layout(
        content=request_data.content, custom_params=request_data.layout_customization
    )
    output_file = service.create_presentation_from_layout(layout=layout)
    return output_file


def generate_presentation_content(request_data: ContentGenerationRequest):
    service = ContentGenerationService()
    content = service.generate_content(
        request_data.topic, custom_params=request_data.content_customization
    )
    return content


def download_presentation_service(request_data: DownloadFileRequest):
    filename = os.path.basename(request_data.filepath)
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return FileResponse(
        request_data.filepath,
        headers=headers,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
