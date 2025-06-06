from libs.utils.common.file_helpers.helpers import read_file

layout_generation_instructions_path = (
    "libs/PPTMaker/platform/modules/bot/src/prompts/layout_gen.md"
)
LAYOUT_GENERATION_PROMPT = read_file(layout_generation_instructions_path)


customize_content_instructions_path = (
    "libs/PPTMaker/platform/modules/bot/src/prompts/customize_content.md"
)
CUSTOMIZE_CONTENT_PROMPT = read_file(customize_content_instructions_path)
