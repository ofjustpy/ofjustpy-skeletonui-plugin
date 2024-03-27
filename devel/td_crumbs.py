from html_writer.macro_module import macros, writer_ctx
import ofjustpy as oj

oj.set_style("un")

with writer_ctx:
    with Div(extra_classes="card text-token", classes="p-4  flex justify-center") as breadcrumb_bar_box:
        with Ol(extra_classes="breadcrumb"):
            with Li(extra_classes="crumb"):
                with A(extra_classes="anchor", href="#", text="Skeleton"):
                    pass
                pass
            with Li(extra_classes="crumb-separator", inner_html="&rsaquo;"):
                pass
            with Li(extra_classes="crumb"):
                with A(extra_classes="anchor", href="#", text="Elements"):
                    pass
                pass
            with Li(extra_classes="crumb-separator", inner_html="&rsaquo;"):
                pass
            
                
html_separator_frame = oj.PD.Subsubsection("With html separator",
                    breadcrumb_bar_box)

with writer_ctx:
    with Div(extra_classes="card text-token", classes="p-4  flex justify-center") as breadcrumb_bar_box:
        with Ol(extra_classes="breadcrumb"):
            with Li(extra_classes="crumb"):
                with A(extra_classes="anchor", href="#", text="Skeleton"):
                    pass
                pass
            with Li(extra_classes="crumb-separator"):
                with FontAwesomeIcon(extra_classes="",
                                     label="faAngleRight", size="1x", 
                                     fixedWidth=True,

                                     ):
                    pass
                pass
            with Li(extra_classes="crumb"):
                with A(extra_classes="anchor", href="#", text="Elements"):
                    pass
                pass
            with FontAwesomeIcon(extra_classes="crumb-separator",
                                 label="faAngleRight", size="1x", 
                                 fixedWidth=True,
                                 
                                 ):
                pass
            
icon_separator_frame = oj.PD.Subsubsection("With Icon separator",
                    breadcrumb_bar_box)

endpoint = oj.create_endpoint(key="td_skeleton_ui",
                   childs = [html_separator_frame,
                             icon_separator_frame
                             ],
                              data_theme= 'data-theme="skeleton"',
                   title = "skeleton ui"
                   )
oj.add_jproute("/", endpoint)
