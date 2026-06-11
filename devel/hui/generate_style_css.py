from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css
target_module = "runner"
#target_module = "td_debug"
themes = [
    "catppuccin",
    "cerberus",
    "concord",
    "crimson",
    "fennec",
    "hamlindigo",
    "legacy",
    "mint",
    "modern",
    "mona",
    "nosh",
    "nouveau",
    "pine",
    "reign",
    "rocket",
    "rose",
    "sahara",
    "seafoam",
    "terminus",
    "vintage",
    "vox",
    "wintry"
]


build_ssr_style_css(target_module,
                    enable_skui_theme_selector = True,
                    additional_skui_themes = themes,
                    output_dir="./static/ssr/")
