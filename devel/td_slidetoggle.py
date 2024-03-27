import ofjustpy as oj
from skeletonui_components.components import SlideToggle
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

slidetoggle= SlideToggle(key="slidetoggle", checked=True)

slidetoggle_inactive_background= SlideToggle(key="slidetoggle", checked=True,
                         background="variant-filled")
app = oj.load_app()

tlc = oj.PD.Container(childs=[slidetoggle,
                                     slidetoggle_inactive_background
                        ],
                twsty_tags=[space/y/4, mr/x/auto]
                )
wp_endpoint = oj.create_endpoint(key="slidetoggle",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="SlideToggle Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
