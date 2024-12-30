#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 17:33:34 2024

@author: princesamee
"""

BLACK = '30'  # ANSI escape code for black letters
RED = '31'  # ANSI escape code for red letters
GREEN = '32'  # ANSI escape code for green letters
YELLOW = '33'  # ANSI escape code for yellow letters
BLUE = '34'  # ANSI escape code for blue letters
VIOLET = '35'  # ANSI escape code for violet letters
LIGHTBLUE = '36'  # ANSI escape code for light blue letters
GREY = '37'  # ANSI escape code for grey letters

BG_BLACK = '40'  # ANSI escape code for black background
BG_RED = '41'  # ANSI escape code for red background
BG_GREEN = '42'  # ANSI escape code for green background
BG_YELLOW = '43'  # ANSI escape code for yellow background
BG_BLUE = '44'  # ANSI escape code for blue background
BG_VIOLET = '45'  # ANSI escape code for violet background
BG_LIGHTBLUE = '46'  # ANSI escape code for light blue background
BG_GREY = '47'  # ANSI escape code for grey background


def colored_text_with_bg(text: str, bg_color_code: str, text_color_code: str = "30"):
    """
    It receives a text, color of the text and color of background
    to change color and returns a format string.

    By default text_color_code is Black and bg_color_code is White (transparent).

    text_color_code
    ---------------
        - BLACK     # ANSI escape code for black letters
        - RED       # ANSI escape code for red letters
        - GREEN     # ANSI escape code for green letters
        - YELLOW    # ANSI escape code for yellow letters
        - BLUE      # ANSI escape code for blue letters
        - VIOLET    # ANSI escape code for violet letters
        - LIGHTBLUE # ANSI escape code for light blue letters
        - GREY      # ANSI escape code for grey letters

    bg_color_code
    -------------
        - BG_BLACK      # ANSI escape code for black background
        - BG_RED        # ANSI escape code for red background
        - BG_GREEN      # ANSI escape code for green background
        - BG_YELLOW     # ANSI escape code for yellow background
        - BG_BLUE       # ANSI escape code for blue background
        - BG_VIOLET     # ANSI escape code for violet background
        - BG_LIGHTBLUE  # ANSI escape code for light blue background
        - BG_GREY       # ANSI escape code for grey background

    Example usage
    +++++++++++++
    ``black_text_on_yellow_bg = colored_text_with_bg("Hello", BG_YELLOW)``

    ``grey_text_on_violet_bg = colored_text_with_bg("Wordl! ", BG_VIOLET, GREY)``

    ``red_text_on_grey_bg = colored_text_with_bg("Goodbye!", BG_GREY, RED)``

    ``print(black_text_on_yellow_bg, grey_text_on_violet_bg, red_text_on_grey_bg)``
    """
    return f"\033[{text_color_code};{bg_color_code}m{text}\033[0m"
