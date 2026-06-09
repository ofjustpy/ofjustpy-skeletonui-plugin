from twtags_safelist import get_twtags_safelist
from svelte_bundler import build_ssr_style_css
#target_module = "td_svg_components"
target_module = "kavya_theme_selector_via_pure_javascript"

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
                    output_dir="./static/ssr/",
                    enable_skui_theme_selector = True,
                    additional_skui_themes = themes
                    )
