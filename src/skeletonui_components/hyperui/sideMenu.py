import ofjustpy as oj
from ofjustpy import icons
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray

from html_writer.macro_module import macros, writer_ctx


def Simple(logo=None, twsty_tags=[], **kwargs):
    with writer_ctx:
        with Div(classes=f"bg-green-100 w-80 h-screen flex flex-col border-e {tstr(*twsty_tags)}",
                 extra_classes="variant-ringed-success bg-green-200"
                 ) as comp_box:

            with Div(classes="flex justify-center  mt-4"):
                with Span(extra_classes="p-4 text-xl text-center card font-bold variant-soft-success", text=logo):
                    pass
                
            with Ul(classes="mt-6 flex-1") as menu_box:
                pass
    def add_flat_item(key,
                      label,
                      menu_box=menu_box,
                      **kwargs):
        with writer_ctx:
            with Li(classes="flex justify-center px-4 py-2",
                    extra_classes=""
                    ) as item_box:
                with Button(key=key,
                            extra_classes="card variant-soft-success",
                            
                            classes= "p-2 hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/5 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hover:shadow-indigo-300", text=label, **kwargs):
                    pass

        menu_box.components.append(item_box)
 
        pass
    comp_box.add_flat_item = add_flat_item        
    return comp_box
