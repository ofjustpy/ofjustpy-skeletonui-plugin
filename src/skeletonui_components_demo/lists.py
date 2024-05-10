import ofjustpy as oj
from py_tailwind_utils import *

from html_writer.macro_module import macros, writer_ctx


with writer_ctx:
     with Mutable_Section(key="unordered_list",
                          classes="w-full p-4 space-y-4",
                          extra_classes="card text-token variant-soft-tertiary") as ul_box:
        with Prose(classes="font-bold", text="Unordered List"):
            pass
        with Ul(extra_classes="list", classes="w-96 space-y-2"):
            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Lisa Hayes"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Erin Gusikowski"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2"):
                with Div(classes="flex space-x-2 items-center"):
                    with Img(src = "https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
                             width=28
                             ):
                        pass
                    with Span(classes="flex-auto", text="Melanie Heller"):
                        pass
                with Span(inner_html="⋮"):
                    pass                                

ul_box_section = oj.Halign(ul_box,
                           content_type="mutable"
                           )

with writer_ctx:
    with Mutable_Div(key="ordered_list",
                     classes="w-full p-4 space-y-4",
                     extra_classes="card text-token variant-soft-tertiary") as ordered_list_box:
        with Prose(classes="font-bold", text="Ordered List"):
            pass
        with Ol(classes="w-96 space-y-2", extra_classes="list"):
            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="1"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item A"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="2"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item B"):
                        pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center", extra_classes="variant-filled-primary m-2"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(extra_classes="badge-icon variant-soft-primary", classes="", text="3"):
                        pass
                    with Span(classes="flex-auto", text="Numbered Item C"):
                        pass
                with Span(inner_html="⋮"):
                    pass                                

ol_box_section =  oj.Halign(ordered_list_box, content_type="mutable"
                            )

with writer_ctx:
    with Mutable_Div(key="desc_list",
                     classes="w-full p-4 space-y-4",
                     extra_classes="text-token card variant-soft-tertiary") as dl_box:
        with Prose(classes="font-bold",
                   text="Description List"):
            pass
        
        with Dl(extra_classes="list-dl w-96 space-y-2"):
            with Li(classes="flex justify-between items-center", extra_classes="variant-filled-primary m-2"):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(classes="p-4", extra_classes="badge-icon variant-soft-secondary"):
                        with FontAwesomeIcon(label="faBook"):
                            pass
                        pass
                    with Span(classes="flex-auto"):
                        with Dt(classes="font-bold", text= "Item A"):
                            pass
                        with Dd(classes="text-sm opacity-50", text="Description for Item A"):
                            pass
                with Span(inner_html="⋮"):
                    pass

            with Li(classes="flex justify-between items-center ", extra_classes="variant-filled-primary m-2 "):
                with Div(classes="space-x-2 items-center flex"):
                    with Span(classes="p-4", extra_classes="badge-icon variant-soft-secondary"):
                        with FontAwesomeIcon(label="faBook"):
                            pass
                        pass
                    with Span(classes="flex-auto"):
                        with Dt(classes="font-bold", text= "Item A"):
                            pass
                        with Dd(classes="text-sm opacity-50", text="Description for Item A"):
                            pass
                with Span(inner_html="⋮"):
                    pass

                
dl_box_section = oj.Halign(dl_box, content_type="mutable"
                                                       )


lists_box = oj.Mutable.Div(key="Listsbox",
               childs = [ul_box_section,
                         ol_box_section,
                         dl_box_section],
               extra_classes="variant-ghost-tertiary w-full card p-4 space-y-4 flex flex-col items-center"
               )
