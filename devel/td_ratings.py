import skeletonui_components as SKUI
import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

oj.set_style("un")
def on_click(dbref, msg, to_ms):
    print("rating clicked ", msg)
    pass
ratings_one = SKUI.Ratings(key="ratings_1", max=5,  interactive=True, on_click = on_click)
# ratings.set_slot_half(FontAwesomeIcon(label="faStarHalfStroke", size="1x")

#                        )
# ratings.set_slot_empty(FontAwesomeIcon(label="faStar", size="1x", fa_group = "regular")

#                        )

# ratings.set_slot_full(FontAwesomeIcon(label="faStar", size="1x")

#                        )
ratings_two = SKUI.Ratings(key="ratings_2", max=5,  interactive=True, on_click = on_click)


app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="accordion",
                                 childs = [                                           
                                           ratings_one,
                                     ratings_two
                                           ],
                                 
                                 title="Accordion"
                                 )
oj.add_jproute("/", wp_endpoint)
