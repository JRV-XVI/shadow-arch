#!/bin/sh

BLANK='#2a000000'       # Almost invisible background, still based on the main background (#2a0000)
CLEAR='#ffcc8033'       # Semi-transparent light golden-orange (from bright yellow)
DEFAULT='#ff8c33cc'     # Warm golden-orange (from normal yellow), now used as the default
TEXT='#ff751fcc'        # Bright vivid orange (from bright green), for readable text
WRONG='#ff0000ee'       # Pure bright red, more intense and opaque for visibility
VERIFYING='#ff3300ee'   # Bright red-orange, but more opaque than antes
KEYHL='#ff2200ff'       # Very strong red highlight when typing
BSHL='#cc0000ff'        # Deep red for backspace highlight (error correction)


i3lock \
--insidever-color=$CLEAR     \
--ringver-color=$VERIFYING   \
\
--insidewrong-color=$CLEAR   \
--ringwrong-color=$WRONG     \
\
--inside-color=$BLANK        \
--ring-color=$DEFAULT        \
--line-color=$BLANK          \
--separator-color=$DEFAULT   \
\
--verif-color=$TEXT          \
--wrong-color=$TEXT          \
--time-color=$TEXT           \
--date-color=$TEXT           \
--layout-color=$TEXT         \
--keyhl-color=$KEYHL         \
--bshl-color=$BSHL           \
\
--screen 1                   \
--blur 5                     \
--clock                      \
--indicator                  \
--time-str="%I:%M:%S"        \
--date-str="%A, %d-%m-%Y"    \
--keylayout 1                \
