import ofjustpy as oj
from skeletonui_components.components import ListBoxItem, ListBox
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *



lbi1 =ListBoxItem(text="Books", value="books")
lbi1.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              ))

lbi =ListBoxItem(text="Movies", value="movies")
lbi.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              ))
lb = ListBox(childs=[lbi, lbi1])

app = oj.load_app()

tlc = oj.PD.Container(childs=[lb
                        ],
                twsty_tags=[space/y/4, mr/x/auto]
                )
wp_endpoint = oj.create_endpoint(key="listbox",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="ListBox Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
