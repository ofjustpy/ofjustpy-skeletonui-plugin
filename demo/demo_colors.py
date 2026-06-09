import ofjustpy as oj
import demo_uisty

from html_writer.macro_module import macros, writer_ctx
from py_tailwind_utils import *
app = oj.load_app()


colors = [green, blue, primary, secondary, tertiary, success, warning, error, surface]

shades = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

childs = []
for c in colors:
    for s in shades:
        childs.append(oj.PD.Div(twsty_tags=[bg/c/s, W/64, H/8]
                                )
                      )




tlc = oj.PD.StackW(childs = childs,
             twsty_tags=[space/x/8, space/y/8]

)

endpoint = oj.create_endpoint("demo_forms",
                              childs = [tlc],
                              csr_bundle_dir="browser_bundle",
                              skeleton_data_theme="seafoam"                            
                              )


oj.add_jproute("/", endpoint)
        
