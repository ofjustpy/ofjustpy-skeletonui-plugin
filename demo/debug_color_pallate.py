
import ofjustpy as oj
import demo_uisty

from html_writer.macro_module import macros, writer_ctx
from py_tailwind_utils import *
app = oj.load_app()


shades = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

c = primary
colors = [green, blue, primary, secondary, tertiary, success, warning, error, surface]
all_colorbars = []

for c in colors:
    childs=[]
    for s in shades:
        childs.append(oj.PD.Div(twsty_tags=[bg/c/s, W/64, H/8]
                                )
                      )
    colorbar=oj.PD.StackH(childs=childs, twsty_tags=[space/x/4])
    all_colorbars.append(colorbar)


tlc = oj.PD.StackV(childs=all_colorbars, twsty_tags=[space/y/4])

with oj.TwStyCtx(demo_uisty):
    abtn1 = oj.AD.Button(key='abtn1', twsty_tags=[pfilled/primary/500]

                        )
    abtn2 = oj.AD.Button(key='abtn2', twsty_tags=[pfilled/primary/"100-900"]

                        )
    abtn3 = oj.AD.Button(key='abtn3', twsty_tags=[pfilled/primary/"400-600"]

                         )

endpoint = oj.create_endpoint("demo_color_pallate",
                              childs = [tlc, abtn1, abtn2, abtn3
                                        ],
                              csr_bundle_dir="browser_bundle",
                              skeleton_data_theme="sahara"                            
                              )


oj.add_jproute("/", endpoint)
        
