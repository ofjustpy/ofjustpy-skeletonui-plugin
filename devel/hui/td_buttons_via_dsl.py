import ofjustpy as oj
#import hyperui_plugin as hui

from html_writer.macro_module import macros, writer_ctx

with writer_ctx:
    with SKHUI.button_wideWithIcon(href="#", text="SkeletonUI") as button_box:
        pass


wp_endpoint = oj.create_endpoint(key="hui_buttons",
                                 childs = [button_box

                                           ],
                                 
                                 title="Buttons",
                                 skeleton_data_theme="modern"
                                 )
oj.add_jproute("/", wp_endpoint)
