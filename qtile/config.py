import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget import UPowerWidget

# Custom script for qtile
from keys import keys, mod, groups, mouse
from themes import Midnight, Tomorrow, RedBlack, RedBlackV2


@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([script])


home = os.path.expanduser("~")
theme = RedBlackV2
accent_color = None

# Define the layout options
layout_defaults = {
    "border_width": 2,
    "border_focus": accent_color,
    "border_normal": theme["text_black"],
}
layout_focus = {
    "border_width": 2,
    "border_focus": theme["on"],
    "border_normal": theme["text_black"],
    "margin": 8,
}
layout_focus2 = {
    "border_width": 1,
    "border_focus": theme["on"],
    "border_normal": theme["text_black"],
}

layouts = [
    layout.MonadTall(**layout_focus, name="Tiled"),
    layout.Max(**layout_focus, name="Max"),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadWide(**layout_focus, name="MonaWide"),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Hack Nerd Font Mono",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

icon = lambda char, foreground, background, fontsize: widget.TextBox(
    font="Hack Nerd Font Mono",
    text=char,
    padding=1,
    margin=0,
    fontsize=fontsize,
    background=background,
    foreground=foreground,
    center_aligned=True,
)

powerline = {"decorations": [PowerLineDecoration(path="forward_slash")]}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    font="Hack Nerd Font Mono",
                    text="",
                    fontsize=30,
                    margin=10,
                    padding=2,
                    background=theme["base_bg"],
                    foreground=theme["base_fg"],
                ),
                widget.CurrentLayout(
                    font="Hack Nerd Font Mono",
                    # scale=0.7,
                    padding=5,
                    background=theme["base_bg"],
                    foreground=theme["base_fg"],
                ),
                widget.GroupBox(
                    font="Hack Nerd Font Mono",
                    highlight_method="line",
                    fmt="{}",
                    highlight_color=[theme["wine_deep"], theme["true_black"]],
                    this_current_screen_border=theme["red_dark"],
                    # this_current_screen=theme["base_bg"],
                    # block_highlight_text_color=theme["base_fg"],
                    active=theme["red_pure"],
                    inactive=theme["red_wine"],
                    background=theme["base_bg"],
                    borderwidth=1,
                    rounded=True,
                    padding_x=10,
                    padding_y=8,
                    margin_x=2,
                    disable_drag=True,
                    center_aligned=True,
                    hide_unused=True,
                    # visible_groups=['1', '2', '3'],
                    # margin=0
                ),
                widget.WindowName(
                    format="{name}",
                    font="Hack Nerd Font Mono",
                    fontsize=16,
                    background=theme["true_black"],
                    foreground=theme["base_fg"],
                    center_aligned=True,
                    max_chars=40,
                    **powerline,
                ),
                widget.KeyboardLayout(
                    configured_keyboards=["us", "latam"],
                    display_map={"us": "US", "latam": "ES"},
                    fmt="  {}",
                    foreground=theme["peach"],
                    background=theme["bg1"],
                    fontsize=16,
                    padding=5,
                    update_interval=0.5,
                    **powerline,
                ),
                icon(
                    "\uf021",
                    foreground=theme["amber"],
                    background=theme["bg1"],
                    fontsize=25,
                ),
                widget.CheckUpdates(
                    distro="Arch",
                    font="Hack Nerd Font Mono",
                    fontsize=14,
                    dislpay_format="{updates}",
                    no_update_string="Updates:0",
                    colour_no_updates=theme["amber"],
                    colour_have_updates=theme["amber"],
                    background=theme["bg1"],
                    foreground=theme["base_fg"],
                    update_interval=10,
                    padding=5,
                    **powerline,
                    mouse_callbacks={
                        "Button1": lazy.spawn(f"alacritty -e sudo pacman -Syu")
                    },
                ),
                icon(
                    "\uf1eb",
                    foreground=theme["golden_red"],
                    background=theme["bg2"],
                    fontsize=25,
                ),
                widget.Net(
                    interface="wlp0s20f3",
                    format="{down}k",
                    background=theme["bg2"],
                    prefix="k",
                    foreground=theme["golden_red"],
                    font="Hack Nerd Font Mono",
                    fontsize=14,
                    padding=5,  # Adjust the padding as needed
                    **powerline,
                ),
                widget.Volume(
                    emoji=True,
                    emoji_list=["\uf00d", "\uf026", "\uf027", "\uf028"],
                    fontsize=30,
                    foreground=theme["golden_red"],
                    background=theme["bg3"],
                ),
                widget.Volume(
                    foreground=theme["golden_red"], background=theme["bg3"], **powerline
                ),
                UPowerWidget(
                    battery_width=25,
                    battery_height=12,
                    background=theme["bg4"],
                    foreground=theme["gray10"],
                    fill_normal=theme["green_pure"],
                    fill_low=theme["amber"],
                    fill_critical=theme["red_pure"],
                    border_colour=theme["gray10"],
                    border_charge_colour=theme["yellow_warm"],
                    margin=3,
                    text_displaytime=6,
                    **powerline,
                ),
                icon(
                    "\uf017",
                    foreground=theme["peach"],
                    background=theme["bg5"],
                    fontsize=25,
                ),
                widget.Clock(
                    font="Hack Nerd Font Mono",
                    format=" %I:%M %p | %d/%m/%y",
                    background=theme["bg5"],
                    foreground=theme["peach"],
                    fontsize=16,
                    center_aligned=True,
                    **powerline,
                ),
                widget.QuickExit(
                    default_text="\uf011",
                    fontsize=24,
                    foreground=theme["red_pure"],
                    background=theme["bg6"],
                    **powerline,
                ),
            ],
            30,
            background=theme["bg6"],
        ),
        # Set static wallpaper
        wallpaper="~/Pictures/wallpapers/saber-alter5.jpg",
        wallpaper_mode="fill",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
