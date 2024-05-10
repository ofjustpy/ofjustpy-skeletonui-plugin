import ofjustpy as oj
import skeletonui_components as SKUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

lbi1 =SKUI.ListBoxItem(text="Books", value="books")
lbi1.set_slot_lead(FontAwesomeIcon(label="faSkull",
                                   size="1x", 
                                   classes="text-xl w-6 text-center",
                                            
                              )
                   )

lbi2 = SKUI.ListBoxItem(text="Movies",
                        value="movies"
                        )

lbi2.set_slot_lead(FontAwesomeIcon(label="faSkull",
                                   size="1x", 
                                   classes="text-xl w-6 text-center",
                                            
                              )
                   )

lbi3 = SKUI.ListBoxItem(text="Parks",
                        value="parks")

lbi3.set_slot_lead(FontAwesomeIcon(label="faSkull",
                                   size="1x", 
                                   classes="text-xl w-6 text-center",
                                            
                              )
                   )

lb = SKUI.ListBox(childs=[lbi1, lbi2, lbi3]
                  )

listbox_box= oj.HCCStatic.Div(key="Listbox",
                              childs=[lb],
                              extra_classes="w-full card p-4 text-token"
                              )
