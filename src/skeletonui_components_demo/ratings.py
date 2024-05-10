import skeletonui_components as SKUI
import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

oj.set_style("un")
def on_click(dbref, msg, to_ms):
    print("rating clicked ", msg)
    pass
ratings_one = SKUI.Ratings(key="ratings_1", max=5,  interactive=True, on_click = on_click)
ratings_two = SKUI.Ratings(key="ratings_2", max=10,  interactive=True, on_click = on_click)


ratings_box= oj.HCCStatic.Div(key="Ratingsbox",
                              childs=[ratings_one,
                                      ratings_two],
                              extra_classes="variant-ghost-tertiary w-full card p-4"
                              )

