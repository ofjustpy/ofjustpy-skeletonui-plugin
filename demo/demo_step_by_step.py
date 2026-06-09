import logging
import macropy.activate
from py_tailwind_utils import *
import ofjustpy as oj

app = oj.load_app()
logger = logging.getLogger(__name__)

oj.set_style("un")
#import skeletonui_components as SKUI
#from hyperui_plugin.selects import  (Base, BaseGroup, Datalist)

async def on_theme_select(dbref, msg, to_ms):
    await msg.page.run_javascript(f"""
    console.log("start setting ");
    const body = document.querySelector('body');
    console.log(body);
    body.setAttribute('data-theme', '{msg.value}');
    console.log("Done setting ");
    """)
    pass

# select_theme_box  = Base("theme-selector",
#                                       "Select Theme",
#                                       on_change=on_theme_select)
# select_theme_box.add_option('skeleton', 'skeleton')
# select_theme_box.add_option('modern', 'modern')
# select_theme_box.add_option('wintry', 'wintry')
# select_theme_box.add_option('rocket', 'rocket')
# select_theme_box.add_option('seafoam', 'seafoam')
# select_theme_box.add_option('vintage', 'vintage')
# select_theme_box.add_option('sahara', 'sahara')
# select_theme_box.add_option('crimson', 'crimson')
# select_theme_box.add_option('mona', 'mona')


# Create Options
skeleton_option = oj.PC.Option(value="skeleton", label="Skeleton", twsty_tags=[bg/green/100])
modern_option = oj.PC.Option(value="modern", label="Modern", twsty_tags=[bg/blue/400])
wintry_option = oj.PC.Option(value="wintry", label="Wintry")
rocket_option = oj.PC.Option(value="rocket", label="Rocket")
seafoam_option = oj.PC.Option(value="seafoam", label="Seafoam")
vintage_option = oj.PC.Option(value="vintage", label="Vintage")
sahara_option = oj.PC.Option(value="sahara", label="Sahara")
crimson_option = oj.PC.Option(value="crimson", label="Crimson")
mona_option = oj.PC.Option(value="mona", label="Mona")

# List of Options
theme_options = [
    skeleton_option, modern_option, wintry_option, rocket_option, 
    seafoam_option, vintage_option, sahara_option, crimson_option, mona_option
]

# Create Select component
select_theme_box = oj.AC.Select(
    key="theme-selector",
    childs=theme_options,
    name="theme-selector",
    form="theme-form",
    required=True,
    size=1,
    default="skeleton",
    twsty_tags=[bg/gray/50, W/64, *encode_twstr("rounded-md border border-gray-300 focus:ring-blue-500 focus:border-blue-500 text-gray-700")],
    on_change=on_theme_select
)


top_bar = oj.PD.Div(twsty_tags=[W/full,
                                db.f,
                                jc.end,
                                space/x/4,
                               
                                ],
                    extra_classes=" bg-gradient-to-br variant-gradient-tertiary-primary",
                    childs=[select_theme_box]
                    )

body_box = oj.PD.Halign(oj.PD.Valign(oj.PD.Span(text="No Stones unturned")),
                        twsty_tags=[W/full]

                        )


endpoint = oj.create_endpoint("Skeleton-ComponentUI",
                     
                              childs = [top_bar,
                                        body_box
                                        ],
                              title="Skeleton Component UI",
                              #page_ready = on_page_ready,
                              csr_bundle_dir="skeletonui"
                              )
oj.add_jproute("/skeletonUI", endpoint)
