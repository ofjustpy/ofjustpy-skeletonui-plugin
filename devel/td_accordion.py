import ofjustpy as oj
from skeletonui_components.components import Accordion, AccordionItem, TabGroup, Tab

from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *
accordionitem = AccordionItem(open=True)
accordionitem.set_slot_lead(FontAwesomeIcon(label="faSkull", size="1x", 
                                            classes="text-xl w-6 text-center",
                                            
                              )
                            )

accordionitem.set_slot_summary(oj.PD.Prose(text="What is Día de los Muertos?", classes="font-bold")
                            )

accordionitem.set_slot_iconClosed(FontAwesomeIcon(label="faMinus", size="1x", 
                                            classes="",
                                            
                              )
    )


accordionitem.set_slot_iconOpen(FontAwesomeIcon(label="faPlus", size="1x", 
                                            classes="",
                                            
                              )
    )

accordionitem.set_slot_content(oj.PD.Prose(text="While Halloween and Day of the Dead occur nearly in tandem and share similar customs (candy, face painting, and community gathering), the two are not related. Halloween has ancient Celtic roots, while Day of the Dead has its own origins that date back to the Indigenous people of Mexico and Central America."))

# 'disabled', 'padding', 'hover', 'rounded', 'regionControl', 'regionPanel', 'regionCaret'
accordion_box = oj.PD.Div(disabled=False, padding="py-2 px-4",
                          hover="hover:bg-primary-hover-token",
                          rounded= "rounded-container-token",
                          regionControl = "",
                          regionPandel="",
                          regionCaret="",
                          childs=[Accordion(childs=[accordionitem],
                                            extra_classes="card text-token",
                                            twsty_tags=[pd/4]
                                            )
                                  ]
                          )

tabgroup_box = oj.PD.Section(classes="w-full p-4", extra_classes="card text-token variant-filled-primary",
              childs= [TabGroup(childs=[Tab(key="Books", text="Books", tab_value=0),
                                        Tab(key="Movies", text="Movies", tab_value=1),
                                        ],
                                active="border-b-4 border-surface-50-900-token"
                                )
                       ],
                             
              )

app = oj.load_app()

wp_endpoint = oj.create_endpoint(key="accordion",
                                 childs = [                                           tabgroup_box
                                  #         accordion_box
                                           ],
                                 
                                 title="Accordion"
                                 )
oj.add_jproute("/", wp_endpoint)
                
