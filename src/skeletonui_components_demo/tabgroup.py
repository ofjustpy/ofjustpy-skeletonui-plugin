from skeletonui_components.components import TabGroup, Tab
import ofjustpy as oj
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

tabgroup = TabGroup(childs=[Tab(key="Books", text="Books", tab_value=0),
                            Tab(key="Movies", text="Movies", tab_value=1),
                            Tab(key="Television", text="Television", tab_value=2),
                                        ],
                    
                                active="border-b-4 border-surface-50-900-token"
                                )


tabgroup.set_slot_panel(oj.PD.Prose(text="A written or printed work consisting of pages glued or sewn together along one side and bound in covers."),
                        oj.PD.Prose(text="A story or event recorded by a camera as a set of moving images and shown in a theater or on television; a motion picture."),
                        oj.PD.Prose(text="A system for transmitting visual images and sound to screens, chiefly for entertainment, information, and education"),
                        
                        
                        )

tabgroup_box = oj.HCCStatic.Div(key="Tabgroupbox",
                              childs=[tabgroup],
                              extra_classes="variant-ghost-tertiary w-full card p-4"
                              )
