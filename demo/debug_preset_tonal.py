import ofjustpy as oj
import demo_uisty

from html_writer.macro_module import macros, writer_ctx
from py_tailwind_utils import *

#7shades = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

all_tonal_childs = []    
for color in  [primary, secondary, tertiary, success, warning, error, surface]:
    all_tonal_childs.append(oj.PD.Div(twsty_tags = [ptonal/color, W/8, H/16]))




endpoint = oj.create_endpoint("demo_presets",
                              childs = [oj.PD.StackH(childs=all_tonal_childs, twsty_tags=[space/x/4])],
                              csr_bundle_dir="browser_bundle",
                              skeleton_data_theme="sahara"                            
                              )


oj.add_jproute("/", endpoint)

    
    
