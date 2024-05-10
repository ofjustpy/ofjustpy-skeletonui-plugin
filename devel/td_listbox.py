import ofjustpy as oj
import skeletonui_components as SKUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *



lbi1 =SKUI.ListBoxItem(text="Books", value="books")
lbi1.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              ))

lbi2 = SKUI.ListBoxItem(text="Movies", value="movies")
lbi2.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              ))

lbi3 = SKUI.ListBoxItem(text="Parks", value="parks")
lbi3.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              ))
lb = SKUI.ListBox(childs=[lbi1, lbi2, lbi3])

app = oj.load_app()

tlc = oj.PD.Container(childs=[lb
                        ],
                twsty_tags=[space/y/4, mr/x/auto]

                      )
app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="listbox",
                                 childs = [ tlc                                          
                                     
                                           ],
                                 
                                 title="ListBox Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                
