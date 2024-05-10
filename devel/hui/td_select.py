import macropy.activate
from skeletonui_components.hyperui import Base
import ofjustpy as oj
from py_tailwind_utils import *

oj.set_style("un")

def on_select(*args, **kwargs):
    pass

select_box  = Base("theme-selector",
                   "Select Theme",
                   on_change=on_select,
                   twsty_tags=[W/128]
                   )


select_box.add_option('skeleton', 'skeleton')
select_box.add_option('modern', 'modern')
select_box.add_option('wintry', 'wintry')

select_box = oj.PD.Valign(oj.PD.Halign(select_box,
                                       twsty_tags=[W/full])
                          )
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="SKUI_HUI_Select",
                                 childs = [ select_box
                                     
                                           ],
                                 
                                 title="SelectBox Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
