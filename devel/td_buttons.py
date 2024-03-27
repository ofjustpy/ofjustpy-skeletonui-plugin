import ofjustpy as oj
from py_tailwind_utils import *
import macropy.activate
from hui_components import Base

app = oj.load_app()
oj.set_style("un")

# ======================= top bar  select theme ======================
async def on_theme_select(dbref, msg, to_ms):
    print ("theme selector changed:", msg.value)
    print(f"""
    console.log("start setting ");
    const body = document.querySelector('body');
    if (body.getAttribute('data-theme') === 'skeleton') {{
    body.setAttribute('data-theme', '{msg.value}');
    }} else {{
    body.setAttribute('data-theme', 'skeleton');
    }}
    console.log("Done setting ");
    """)
    
    await msg.page.run_javascript(f"""
    console.log("start setting ");
    const body = document.querySelector('body');
    console.log(body);
    if (body.getAttribute('data-theme') === 'skeleton') {{
    console.log("X1");
    body.setAttribute('data-theme', '{msg.value}');
        console.log("X2");
    }} else {{
    body.setAttribute('data-theme', 'skeleton');
    }}
    console.log("Done setting ");
    """)
    pass

select_box  = Base("theme-selector", "Select Theme", on_change=on_theme_select)
select_box.add_option('skeleton', 'skeleton')
select_box.add_option('modern', 'modern')
select_box.add_option('wintry', 'wintry')

select_box.add_option('rocket', 'rocket')
select_box.add_option('seafoam', 'seafoam')
select_box.add_option('vintage', 'vintage')
select_box.add_option('sahara', 'sahara')
select_box.add_option('crimsom', 'crimson')


top_bar = oj.PD.Div(twsty_tags=[W/full, db.f,  flx.rrow, space/x/4],
          childs=[select_box]
    )

shades = ["",
          "primary",
          "secondary",
          "tertiary",
          "success",
          "warning",
          "error",
          "surface"

    ]
variants = [["variant-filled",
             ],
            

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


variant_filled = oj.PD.Subsubsection("Variant Filled",
                                           oj.PD.StackV(childs = [_ for _ in X()], twsty_tags=[space/y/4])
                                           )

variant_ghost = oj.PD.Subsubsection("Variant Ghost",
                                           oj.PD.StackV(childs = [_ for _ in X("ghost")
                                                                  ],
                                                        twsty_tags=[space/y/4])
                                           )


variant_soft = oj.PD.Subsubsection("Variant Soft",
                                           oj.PD.StackV(childs = [_ for _ in X("soft")
                                                                  ],
                                                        twsty_tags=[space/y/4])
                                           )


variant_ringed = oj.PD.Subsubsection("Variant Ringed",
                                           oj.PD.StackV(childs = [_ for _ in X("ringed")
                                                                  ],
                                                        twsty_tags=[space/y/4])
                                           )

variant_glass = oj.PD.Subsubsection("Variant Glass",
                                           oj.PD.StackV(childs = [_ for _ in X("glass")
                                                                  ],
                                                        twsty_tags=[space/y/4])
                                           )




tlc = oj.PD.Container(childs = [variant_filled,
                                variant_ghost,
                                variant_soft,
                                variant_ringed,
                                variant_glass
                                 
                                ]
                      
                      )

wp_endpoint = oj.create_endpoint(key="sk_buttons",
                                 childs = [top_bar, oj.PD.Br(twsty_tags= [mr/st/4, mr/sb/4]), tlc
                                           ],
                                 
                                 title="Skeleton Buttons"
                                 )


oj.add_jproute("/", wp_endpoint)
