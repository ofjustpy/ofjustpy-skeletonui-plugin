import ofjustpy as oj
from shadcnui_components.dsl  import macros, writer_ctx
import shadcnui_components as SCUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon

oj.set_style("un")

with writer_ctx:
    with SCUI.HoverCard() as hovercard_box:
        
        with SCUI.HoverCard.Trigger():
            with oj.PD.Prose(text="Hover"):
                pass
        
        with SCUI.HoverCard.Content():
            with oj.PD.Prose(text="SvelteKit - Web development, streamlined"):
                pass

            

endpoint = oj.create_endpoint("demo_hover_card",
                              childs = [hovercard_box],
                              csr_bundle_dir="browser_bundle",
                              skeleton_data_theme="mint"                            
                              )


oj.add_jproute("/", endpoint)
                    
