import kavya as kv
from py_tailwind_utils import *
import theme_select_bar
from skeletonui_components.hyperui import Popup
kv.set_style("un")
app = kv.load_app()

alert_popup = Popup('popup',
      title='Your product changes have been saved.', desc='Changes saved'
      )

tlc = kv.HM.Container(childs = [alert_popup
                                ]
                      
                      )

wp_endpoint = kv.create_endpoint(key="alerts",
                                 childs = [theme_select_bar.top_bar,
                                           kv.PD.Br(twsty_tags= [mr/st/4, W/full, H/4, mr/sb/4]),
                                           tlc

                                           ],
                                 
                                 body_classes="font-geist",
                                 skeleton_data_theme="modern",
                                 rendering_type="MutableSSR",
                                 svelte_bundle_dir="ssr" 
                                 )


kv.add_route("/", wp_endpoint)

