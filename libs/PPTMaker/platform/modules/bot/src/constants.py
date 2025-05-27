from libs.utils.common.file_helpers.helpers import read_file

content_generation_instructions_path = (
    "libs/PPTMaker/platform/modules/bot/src/prompts/content_generation.md"
)
CONTENT_GENERATION_PROMPT = read_file(content_generation_instructions_path)


customize_content_instructions_path = (
    "libs/PPTMaker/platform/modules/bot/src/prompts/customize_content.md"
)
CUSTOMIZE_CONTENT_PROMPT = read_file(customize_content_instructions_path)
