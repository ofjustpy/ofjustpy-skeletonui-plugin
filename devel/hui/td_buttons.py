import kavya as kv
from py_tailwind_utils import *
from skeletonui_components.hyperui import buttons
import theme_select_bar

kv.set_style("un")
app = kv.load_app()


hbtn = buttons.wideWithIcon(href="#", text="SkeletonUI")

endpoint = kv.create_endpoint("buttons",
                              childs = [
                                  theme_select_bar.top_bar,
                                  hbtn
                                        ],
                              title="Buttons",
                              skeleton_data_theme="modern",
                              rendering_type="MutableSSR",
                              svelte_bundle_dir="ssr" 
                              
                              )
kv.add_route("/", endpoint)

