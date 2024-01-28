# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen",
    ),
    # Personal keybindings
    Key([mod], "r", lazy.spawn("redshift -O 4000"), desc="turn on redshift"),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x"), desc="turn off redshift"),
    Key(
        [mod],
        "space",
        lazy.spawn("/home/cheto59/.config/rofi/scripts/launcher_t1_windows"),
        desc="look for a window to switch",
    ),
    Key(
        [mod],
        "e",
        lazy.spawn("subl"),
        desc="launch subl",
    ),
    Key(
        [mod],
        "p",
        lazy.spawn("alacritty --command btm"),
        desc="Launch bottom terminal process",
    ),
    Key(
        [mod],
        "m",
        lazy.spawn("/home/cheto59/.config/rofi/scripts/launcher_t1"),
        desc="Launch terminal",
    ),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch Browser"),
    Key(
        [mod],
        "d",
        lazy.spawn("alacritty --command ranger"),
        desc="Launch ranger file manager",
    ),
    Key([mod], "t", lazy.spawn("alacritty -e yazi"), desc="Launch yazi file manager"),
    Key(
        [mod], "s", lazy.spawn("gnome-screenshot -i -c"), desc="Launch gnome-screenshot"
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pamixer -t"),
        desc="Mute Volume",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +10%"),
        desc="Increase Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 10%-"),
        desc="Decrease Brightness",
    ),
    Key(
        [mod],
        "c",
        lazy.spawn(
            "alacritty --working-directory /home/cheto59/.config/qtile --command nvim config.py"
        ),
        desc="Open Qtile configuration file",
    ),
    Key(
        [mod],
        "v",
        lazy.spawn(
            "alacritty --working-directory /home/cheto59/Dev/vagrant/backendclass/"
        ),
    ),
    Key(
        [mod],
        "o",
        lazy.spawn(
            "alacritty --working-directory /home/cheto59/Dev/web/belicodersProject/belicoders_REST_API/"
        ),
    ),
    Key(
        [mod],
        "i",
        lazy.spawn(
            "alacritty --working-directory /home/cheto59/Dev/web/belicodersProject/belicoders/"
        ),
    ),
    Key(
        [mod],
        "u",
        lazy.spawn("keepassxc"),
    ),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

groups = [Group(i) for i in ["", "󰣇", "", "", "", ""]]

for i, group in enumerate(groups):
    workspace_number = str(i + 1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                workspace_number,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                workspace_number,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(margin=15),
    layout.Columns(
        border_normal="#060606",
        border_focus="#ca9ee6",
        border_width=3,
        margin=8,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(margin = 20),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMonoNL Nerd Font", fontsize=15, padding=8, foreground="#a6e3a1"
)
extension_defaults = widget_defaults.copy()

layout_decor = {
    "decorations": [
        RectDecoration(
            colour="#4c4f69",
            radius=5,
            filled=True,
            padding_y=1,
            padding_x=1,
        )
    ],
    "padding": 35,
    "fontsize": 18,
    "foreground": "#e78284",
}

rect_decor = {
    "decorations": [
        RectDecoration(
            colour="#313244",
            radius=5,
            filled=True,
        )
    ]
}


group_box_decor = {
    **rect_decor,
    "disable_drag": True,
    "padding": 10,
    "fontsize": 25,
    "block_highlight_text_color": "#cba6f7",
    "this_current_screen_border": "#313244",
    "this_screen_border": "#313244",
    "active": "#fff",
    "foreground": "#fff",
    "inactive": "#fff",
    "border_width": 0,
}

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(**layout_decor),
                widget.GroupBox(
                    **group_box_decor,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Spacer(),
                widget.Systray(**group_box_decor),
                widget.Clock(**rect_decor, format="%Y-%m-%d %a %I:%M %p", fontsize=16),
            ],
            30,
            opacity=1,
            background="#181825",
            margin=0,
            # border_width=[1, 1, 1, 1],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
