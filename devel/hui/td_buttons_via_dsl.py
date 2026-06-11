import kavya as kv
from kavya.dsl import macros, MuCtx
from py_tailwind_utils import *
import theme_select_bar
from skeletonui_components import hyperui as SKHUI
kv.set_style("un")
app = kv.load_app()


with MuCtx:
    with SKHUI.button_wideWithIcon(href="#", text="SkeletonUI") as button_box:
        pass


wp_endpoint = kv.create_endpoint(key="hui_buttons",
                                 childs = [button_box

                                           ],
                                 
                                 title="Buttons",
                                 skeleton_data_theme="modern"
                                 )
kv.add_route("/", wp_endpoint)
