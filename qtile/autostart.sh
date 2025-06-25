#!/bin/bash
picom --config ~/.config/picom.conf &
autorandr --change
xwinwrap -ov -g 1920x1080 -- mpv -wid WID --panscan=1.0 --no-audio --no-osc --no-osd-bar --no-input-default-bindings --loop ~/Videos/unleashing-sabers-excalibur.mp4 &
