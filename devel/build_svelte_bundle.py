from svelte_bundler.csr import  build_csr_svelte_bundle

build_csr_svelte_bundle("runner",

                        enable_skui_theme_selector = True,
                        additional_skui_themes = [
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

                        )


