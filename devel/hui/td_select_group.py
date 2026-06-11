import kavya as kv
from py_tailwind_utils import *
import theme_select_bar

from skeletonui_components.hyperui import Base, BaseGroup

async def on_select(*args, **kwargs):
    pass

basegroup_select = BaseGroup("basegroup",
                             "Headline",
                             on_change=on_select
                             )
optgroup = basegroup_select.add_optgroup("A")
optgroup.add_option("AK", "Albert King")

optgroup = basegroup_select.add_optgroup("B")
optgroup.add_option("BBK", "B.B King")
optgroup.add_option("BG", "Buddy Guy")


optgroup = basegroup_select.add_optgroup("E")
optgroup.add_option("EC", "Eric Clapton")


optgroup = basegroup_select.add_optgroup("J")
optgroup.add_option("JM", "John Mayer")
optgroup.add_option("JH", "Jimi Hendrix")

optgroup = basegroup_select.add_optgroup("S")
optgroup.add_option("SRV", "Stevie Ray Vaughn")

selectgroup_box = kv.PD.Valign(kv.PD.Halign(basegroup_select,
                                       twsty_tags=[W/full])
                          )
app = kv.load_app()
wp_endpoint = kv.create_endpoint(key="SKUI_HUI_Select",
                                 childs = [
                                     theme_select_bar.top_bar,
                                     selectgroup_box
                                     
                                           ],
                                 
                                 title="SelectBox Demo",
                                 body_classes="font-geist",
                                 skeleton_data_theme="modern",
                                 rendering_type="MutableSSR",
                                 svelte_bundle_dir="ssr" 
                                 )
kv.add_route("/", wp_endpoint)
                
