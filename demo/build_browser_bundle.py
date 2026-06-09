import macropy.activate
from svelte_safelist_builder import get_svelte_safelist

twtags, fontawesome_icons = get_svelte_safelist("runner")
print(twtags)
font_families = ["Geist", "Roboto"]
print(twtags)

# # which font families to include
# font_families = ["Geist", "Roboto"]

from  svelte_bundler import  skeletonui_bundle_builder


skeletonui_bundle_builder(twtags,
                          skui_themes=["seafoam", "mint", "sahara"],
                                    font_families=font_families,
                                    fontawesome_icons = fontawesome_icons,
                                    output_dir="./static/browser_bundle",

                                    )


