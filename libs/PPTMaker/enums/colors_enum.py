from enum import Enum

from pptx.dml.color import RGBColor


class ColorEnum(Enum):
    # Neutrals
    BLACK = RGBColor(0, 0, 0)
    WHITE = RGBColor(255, 255, 255)
    GRAY_DARK = RGBColor(33, 37, 41)
    GRAY_MEDIUM = RGBColor(108, 117, 125)
    GRAY_LIGHT = RGBColor(173, 181, 189)
    GRAY_LIGHTER = RGBColor(158, 158, 158)
    GRAY_DIM = RGBColor(105, 105, 105)
    GRAY_DARKER = RGBColor(89, 89, 89)
    GRAY_EXTRA_DARK = RGBColor(32, 32, 32)
    GRAY_TEXT = RGBColor(178, 178, 178)
    WHITE_SMOKE = RGBColor(245, 245, 245)
    GHOST_WHITE = RGBColor(248, 248, 255)

    # Blues
    BLUE_DARK = RGBColor(31, 73, 125)
    BLUE_MEDIUM = RGBColor(68, 114, 196)
    BLUE_LIGHT = RGBColor(155, 194, 230)
    CLEAN_BLUE = RGBColor(0, 123, 255)
    NAVY_BLUE = RGBColor(0, 32, 96)
    STEEL_BLUE = RGBColor(70, 130, 180)
    LIGHT_STEEL_BLUE = RGBColor(176, 196, 222)
    MIDNIGHT_BLUE = RGBColor(25, 25, 112)
    DARK_SLATE_BLUE = RGBColor(72, 61, 139)
    MEDIUM_SLATE_BLUE = RGBColor(123, 104, 238)

    # Greens
    GREEN_SUCCESS = RGBColor(40, 167, 69)
    GREEN_BRIGHT = RGBColor(40, 167, 69)
    SPRING_GREEN = RGBColor(0, 255, 127)
    DARK_GREEN = RGBColor(0, 100, 0)
    FOREST_GREEN = RGBColor(34, 139, 34)
    LIME_GREEN = RGBColor(50, 205, 50)

    # Reds
    RED = RGBColor(220, 53, 69)
    RED_ORANGE = RGBColor(255, 69, 0)
    TOMATO = RGBColor(255, 99, 71)
    DARK_RED = RGBColor(139, 0, 0)
    FIRE_BRICK = RGBColor(178, 34, 34)

    # Pinks & Purples
    HOT_PINK = RGBColor(255, 105, 180)
    DEEP_PINK = RGBColor(255, 20, 147)
    LIGHT_PINK = RGBColor(255, 182, 193)
    PURPLE = RGBColor(128, 0, 128)
    INDIGO = RGBColor(75, 0, 130)
    DARK_PURPLE = RGBColor(102, 51, 153)

    # Yellows & Oranges
    GOLD = RGBColor(255, 215, 0)
    GOLD_DARK = RGBColor(255, 192, 0)
    YELLOW = RGBColor(255, 255, 0)
    YELLOW_WARNING = RGBColor(255, 193, 7)
    ORANGE = RGBColor(255, 165, 0)
    DARK_ORANGE = RGBColor(255, 140, 0)
    GOLDENROD = RGBColor(218, 165, 32)
    DARK_GOLDENROD = RGBColor(184, 134, 11)

    # Backgrounds
    BACKGROUND_LIGHT = RGBColor(255, 255, 255)
    BACKGROUND_DARK = RGBColor(0, 0, 0)
    BACKGROUND_PINK = RGBColor(244, 194, 194)
    CORNSILK = RGBColor(255, 248, 220)
