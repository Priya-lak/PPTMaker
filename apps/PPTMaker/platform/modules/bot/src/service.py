import os

from fastapi.responses import FileResponse

from apps.PPTMaker.platform.modules.bot.src.dto import (
    DownloadFileRequest,
    PresentationGenerationRequest,
)
from libs.PPTMaker.enums.themes_styles_enum import StylesEnum
from libs.PPTMaker.platform.modules.bot.src.services.ppt_generator_service import (
    PPTGenerator,
)


def create_customized_presentation(request_data: PresentationGenerationRequest):
    ppt_gen_service = PPTGenerator(style=request_data.style, theme=request_data.theme)
    content = ppt_gen_service.generate_content(
        request_data.topic, custom_params=request_data.customization
    )
    output_file = ppt_gen_service.create_presentation_from_content(content=content)
    return output_file


def download_presentation_service(request_data: DownloadFileRequest):
    filename = os.path.basename(request_data.filepath)
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return FileResponse(
        request_data.filepath,
        headers=headers,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
