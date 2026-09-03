import kavya as kv
import demo_uisty


from py_tailwind_utils import *

#7shades = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

shades = [
    "950-50",
    "900-100",
    "800-200",
    "700-300",
    "600-400",
    "500",
    "400-600",
    "300-700",
    "200-800",
    "100-900",
    "50-950"
]

all_preset_childs = []
for preset in [pfilled, poutlined]:
    all_color_childs = []
    for color in  [primary, secondary, tertiary, success, warning, error, surface]:
        all_shades_childs =  []
        for shade in shades:
            adiv = kv.PD.Div(twsty_tags = [preset/color/shade, W/8, H/16],
                      )
            all_shades_childs.append(adiv)

        all_shades_div = kv.PD.StackV(childs=all_shades_childs, twsty_tags=[space/y/4])
        all_color_childs.append(all_shades_div)
    all_color_div = kv.PD.StackH(childs=all_color_childs, twsty_tags=[space/x/4])
    all_preset_childs.append(all_color_div)


all_tonal_childs = []
for color in  [primary, secondary, tertiary, success, warning, error, surface]:
    all_tonal_childs.append(kv.PD.Div(twsty_tags = [ptonal/color, W/8, H/16]))

all_preset_childs.append(kv.PD.StackH(childs=all_tonal_childs, twsty_tags=[space/x/4]))

tlc = kv.PD.StackV(childs = all_preset_childs, twsty_tags=[space/y/4])

endpoint = kv.create_endpoint("demo_presets",
                              childs = [tlc],
                              svelte_bundle_dir="browser_bundle",
                              skeleton_data_theme="seafoam"                            
                              )


kv.add_route("/", endpoint)

    
    
