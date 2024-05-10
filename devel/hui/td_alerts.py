import macropy.activate
from skeletonui_components.hyperui import Popup
import ofjustpy as oj
from py_tailwind_utils import *
import theme_select_bar 
oj.set_style("un")
app = oj.load_app()

alert_popup = Popup('popup',
      title='Your product changes have been saved.', desc='Changes saved'
      )

tlc = oj.HCCMutable.Container(childs = [alert_popup
                                ]
                      
                      )

wp_endpoint = oj.create_endpoint(key="alerts",
                                 childs = [theme_select_bar.top_bar, oj.PD.Br(twsty_tags= [mr/st/4, W/full, H/4, mr/sb/4]),
                                           tlc

                                           ],
                                 
                                 body_classes="font-geist",
                                 skeleton_data_theme="modern"
                                 )


oj.add_jproute("/", wp_endpoint)

