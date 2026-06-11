import macropy.activate 
import kavya as kv
from py_tailwind_utils import *
from hyperui_plugin import selects
from kavya.session_managment import get_comp_target

abtn = kv.PD.Button(text="a big button background",
                    twsty_tags= [W/20, mr/y/4, bg/secondary/500]
                    
                    )


skeleton_colors = [primary, secondary, tertiary, success, warning, error, surface]

skeleton_shades = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
color_palette = [bg/color/shade for color in skeleton_colors for shade in skeleton_shades]

# Generate all possible combinations (7 colors * 11 shades = 77 unique classes)
# Perfect for your 11x7 grid!
#color_palette = [f"bg-{color}-{str(shade)}" for color in skeleton_colors for shade in skeleton_shades]

grid_cells = []
color_index = 0
for row in range(11):
    row_cells = []
    for col in range(7):
        # Create an individual rectangle
        cell_color = color_palette[color_index % len(color_palette)]
        color_index += 1
        rect = kv.PC.Label(twsty_tags=[cell_color], 
                           extra_classes=f"w-16 h-16 rounded m-1",  
        )
        row_cells.append(rect)
    grid_cells.append(row_cells)

    
grid_container = kv.PD.Div(childs=[kv.PD.Div(childs=row, classes="flex flex-row") for row in grid_cells],
                           classes="flex flex-col p-4"
                           )

selector_box = color_utility_class_selector_box = selects.Base("theme_selector", "Choose theme")


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


for  value in themes:
    selector_box.add_option(value=value, text=value)

        
# hack to directly invoke javascript
abtn.htmlRender_attr.append("""onclick="set_skui_theme()"
"""
                            )
abtn.prepare_htmlRender()
# hack/workaround to embed theme_selector event 
select_div = get_comp_target("/theme_selector_select_box")


select_div.htmlRender_attr.append("""onchange="set_skui_theme(this.value)"
"""
                            )
select_div.prepare_htmlRender()
wp_endpoint = kv.create_endpoint(key="webpage_static_ssr",
                                 childs =[grid_container, selector_box],
                                 #body_classes = "bg-slate-100 dark:bg-slate-900",
                                 #html_classes = "font-sans text-gray-800",
                                 svelte_bundle_dir="ssr",
                                 skeleton_data_theme = "rose",
                                 rendering_type="SSR"
                                 )

app = kv.load_app()
kv.add_route("/", wp_endpoint)
# from starlette.testclient import TestClient
# testclient = TestClient(app)

# response = testclient.get(f'/')
# print(response.text)
# assert response.status_code == 200
