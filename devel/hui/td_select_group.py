import macropy.activate
from skeletonui_components.hyperui import Base, BaseGroup
import ofjustpy as oj
from py_tailwind_utils import *

oj.set_style("un")

def on_select(*args, **kwargs):
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

selectgroup_box = oj.PD.Valign(oj.PD.Halign(basegroup_select,
                                       twsty_tags=[W/full])
                          )
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="SKUI_HUI_Select",
                                 childs = [ selectgroup_box
                                     
                                           ],
                                 
                                 title="SelectBox Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
