import ofjustpy as oj
from py_tailwind_utils import *
from skeletonui_components.components import TabGroup, Tab



shades = ["",
          "primary",
          "secondary",
          "tertiary",
          "success",
          "warning",
          "error",
          "surface"

    ]

def X(variant_type = "filled"):
    for shdn in shades:
        pshdn = shdn
        
        if shdn != "":
            pshdn = f"-{shdn}"
        btn_icon = oj.AD.Button(key="ibtn",  childs = [oj.icons.FontAwesomeIcon(label="faSkull", size="2x", 
                                      fixedWidth=True,
                                      )
                               ],
                                type="button", 
                                extra_classes=f"btn-icon variant-{variant_type}{pshdn}"
                     )

        btn_text = oj.AD.Button(key="tbtn", type = "button",
                                extra_classes=f"btn variant-{variant_type}{pshdn}",
                                text="Button"
                                )

        btn_icon_text = oj.AD.Button(key="itbtn", type = "button",
                                     extra_classes=f"btn variant-{variant_type}{pshdn}",
                                     childs = [oj.icons.FontAwesomeIcon(label="faSkull",
                                                               size="2x",
                                                               fixedWidth=True)
                                               ],
                                text="Button"
                                )


        btn_bar = oj.PD.StackH(twsty_tags=[space/x/4], childs=[btn_icon,
                                                               btn_text,
                                                               btn_icon_text

                                                               ]
                               )
        yield btn_bar

        
variant_filled = oj.PD.Subsection("Variant Filled",
                                  oj.PD.StackV(childs = [_ for _ in X()], twsty_tags=[space/y/4]),
                                  section_depth=10
                                           )

variant_ghost = oj.PD.Subsection("Variant Ghost",
                                 oj.PD.StackV(childs = [_ for _ in X("ghost")
                                                        ],
                                              twsty_tags=[space/y/4]),
                                 section_depth=10
                                 )


variant_soft = oj.PD.Subsection("Variant Soft",
                                   oj.PD.StackV(childs = [_ for _ in X("soft")
                                                          ],
                                                twsty_tags=[space/y/4]),
                                section_depth=10
                                           )


variant_ringed = oj.PD.Subsection("Variant Ringed",
                                     oj.PD.StackV(childs = [_ for _ in X("ringed")
                                                                  ],
                                                        twsty_tags=[space/y/4]),
                                  section_depth=10
                                           )

variant_glass = oj.PD.Subsection("Variant Glass",
                                    oj.PD.StackV(childs = [_ for _ in X("glass")
                                                                  ],
                                                 twsty_tags=[space/y/4]),
                                 section_depth=10
                                    )

tabgroup = TabGroup(childs=[Tab(key="Filled", text="Filled", tab_value=0),
                            Tab(key="Soft", text="Soft", tab_value=1),
                            Tab(key="Ghost", text="Ghost", tab_value=2),
                                        ],
                    
                    active="border-b-4 border-surface-50-900-token"
                    )

tabgroup.set_slot_panel(variant_filled,
                        variant_soft,
                        variant_ghost
                        )

frame=oj.PD.StackG(num_cols=2,
                   num_rows=2,
                   childs = [variant_filled,
                             variant_ghost,
                             variant_soft,
                             variant_ringed,
                             # variant_glass
                             
                             ],
                   twsty_tags=[overflowx.auto]
                   )
buttons_box = oj.HCCStatic.Div(key="Buttonsbox",
                     childs = [tabgroup
                                 
                                ],
                               
                               extra_classes="variant-ghost-tertiary card p-4 space-y-4 flex flex-col items-center overflow-x-auto overflow-x-auto"                       
                      )
