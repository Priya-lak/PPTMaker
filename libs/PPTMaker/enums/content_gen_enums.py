from enum import Enum


class ToneEnum(str, Enum):
    PROFESSIONAL = "professional"
    CASUAL = "casual"
    FRIENDLY = "friendly"
    ACADEMIC = "academic"
    PERSUASIVE = "persuasive"
    TECHNICAL = "technical"


class LengthEnum(str, Enum):
    BRIEF = "brief"
    MODERATE = "moderate"
    DESCRIPTIVE = "descriptive"
    COMPREHENSIVE = "comprehensive"


class SlideRangeEnum(str, Enum):
    RANGE_3_5 = "3-5"
    RANGE_6_9 = "6-9"
    RANGE_10_15 = "10-15"
    RANGE_16_PLUS = "16+"


class TargetAudienceEnum(str, Enum):
    EXECUTIVES = "executives"
    STUDENTS = "students"
    GENERAL_PUBLIC = "general"
    TECHNICAL_EXPERTS = "technical_experts"
    CHILDREN = "children"
    PROFESSIONALS = "professionals"
    RESEARCHERS = "researchers"


class PresentationPurposeEnum(str, Enum):
    EDUCATIONAL = "educational"
    SALES_PITCH = "sales_pitch"
    PROJECT_UPDATE = "project_update"
    TRAINING = "training"
    CONFERENCE_TALK = "conference_talk"
    MEETING_PRESENTATION = "meeting_presentation"
    WORKSHOP = "workshop"
    PITCH_DECK = "pitch_deck"


class DetailLevelEnum(str, Enum):
    HIGH_LEVEL_OVERVIEW = "overview"
    MODERATE_DETAIL = "intermediate"
    DEEP_DIVE = "deep_dive"
    EXPERT_LEVEL = "expert_level"


class ExamplesEnum(str, Enum):
    NONE = "none"
    MINIMAL = "minimal"
    MODERATE = "moderate"
    EXTENSIVE = "extensive"


class EngagementLevelEnum(str, Enum):
    INFORMATIONAL = "informational"
    INTERACTIVE = "interactive"
    HIGHLY_ENGAGING = "highly_engaging"


class IndustryEnum(str, Enum):
    TECHNOLOGY = "technology"
    HEALTHCARE = "healthcare"
    FINANCE = "finance"
    EDUCATION = "education"
    MARKETING = "marketing"
    MANUFACTURING = "manufacturing"
    RETAIL = "retail"
    CONSULTING = "consulting"
    GOVERNMENT = "government"
    NON_PROFIT = "non_profit"
    GENERAL = "general"


class VisualPreferenceEnum(str, Enum):
    TEXT_HEAVY = "text_heavy"
    IMAGE_HEAVY = "image_heavy"
    BALANCED = "balanced"
    CHART_FOCUSED = "chart_focused"
    MINIMAL = "minimal"


class DataFocusEnum(str, Enum):
    HEAVY_DATA = "heavy_data"
    MODERATE_STATS = "moderate_stats"
    MINIMAL_NUMBERS = "minimal_numbers"
    DATA_DRIVEN = "data_driven"


class RegionalFocusEnum(str, Enum):
    GLOBAL = "global"
    NORTH_AMERICA = "north_america"
    EUROPE = "europe"
    ASIA_PACIFIC = "asia_pacific"
    LATIN_AMERICA = "latin_america"
    MIDDLE_EAST_AFRICA = "middle_east_africa"
    SPECIFIC_COUNTRY = "specific_country"


class TimeDurationEnum(str, Enum):
    DURATION_5_MIN = "5_min"
    DURATION_15_MIN = "15_min"
    DURATION_30_MIN = "30_min"
    DURATION_45_MIN = "45_min"
    DURATION_1_HOUR = "1_hour"
    DURATION_1_HOUR_PLUS = "1_hour_plus"
