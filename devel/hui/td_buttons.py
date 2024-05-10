import macropy.activate
from skeletonui_components.hyperui import buttons
import ofjustpy as oj
from py_tailwind_utils import *
import theme_bar_wrapper

import ofjustpy as oj
oj.set_style("un")

from ofjustpy import icons
from py_tailwind_utils import *
from ofjustpy import icons

app = oj.load_app()
top_bar = theme_bar_wrapper.get_top_bar()

hbtn = buttons.wideWithIcon(href="#", text="SkeletonUI")

endpoint = oj.create_endpoint("buttons",
                              childs = [
                                  top_bar,
                                  hbtn
                                        ],
                              title="Buttons",
                              skeleton_data_theme="modern"
                              )
oj.add_jproute("/", endpoint)

