import ofjustpy as oj
from py_tailwind_utils import *
import theme_bar_wrapper
oj.set_style("un")
app= oj.load_app()
btn_styled_by_parts_soft = oj.AD.Button(key="styled_by_parts",
                                   extra_classes="btn bg-primary-500 bg-opacity-20 text-primary-700 shadow-ring focus:shadow-ring-focus hover:bg-primary-400 hover:text-primary-600 focus:bg-primary-600 focus:text-primary-800",
                                   text="Button",
                                   twsty_tags=[W/64, H/8]
             )

btn_styled_by_parts_filled = oj.AD.Button(key="styled_by_parts",
                                   extra_classes="btn bg-primary-500 text-primary-100 shadow-ring focus:shadow-ring-focus hover:bg-primary-600 hover:text-primary-200 focus:bg-primary-400 focus:text-primary-300",
                                   text="Button",
                                   twsty_tags=[W/64, H/8]
             )

btn_styled_by_variant = oj.AD.Button(key="tbtn", type = "button",
                                     extra_classes="btn variant-filled-primary",
                                     text="Button",
                                     twsty_tags=[W/64, H/8]
                                  )
top_bar = theme_bar_wrapper.get_top_bar()


endpoint = oj.create_endpoint("buttons",
                              childs = [top_bar,
                                        btn_styled_by_parts_soft,
                                        btn_styled_by_parts_filled,
                                        btn_styled_by_variant 
                                        ],
                              twsty_tags=[space/y/8, db.f, flx.col],
                              title="Buttons",
                              skeleton_data_theme="modern"
                              )
oj.add_jproute("/", endpoint)
