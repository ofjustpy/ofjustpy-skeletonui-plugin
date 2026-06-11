import kavya as kv
from py_tailwind_utils.to_twsty_expr import encode_twstr
from py_tailwind_utils import conc_twtags, tstr, pd, grow, bg, green, W, fc, gray

from kavya.dsl import macros, MuCtx


def Simple(logo=None, twsty_tags=[], **kwargs):
    with MuCtx:
        with Div(classes=f"w-80 h-screen flex flex-col border-e {tstr(*twsty_tags)}",
                 extra_classes="variant-ringed-success"
                 ) as comp_box:

            with Div(classes="flex justify-center  mt-4"):
                with Span(extra_classes="p-4 text-xl text-center card font-bold variant-soft-success", text=logo):
                    pass
                
            with PD.Ul(classes="mt-6 flex-1") as menu_box:
                pass

    def add_group_item(title, menu_box=menu_box):
        with MuCtx:
            with Li(classes='') as group_box:
                with Details(classes='group', extra_classes="[&_summary::-webkit-details-marker]:hidden"):
                    with Summary(classes='flex cursor-pointer items-center justify-between rounded-lg px-4 py-2 text-gray-500 hover:bg-gray-100 hover:text-gray-700'):
                        with Div(classes = "flex-1 flex justify-center"):
                            with Span(classes='px-4 font-bold text-indigo-500 text-large uppercase leading-normal', text=title):
                                pass
                            pass
                        

                        with Span(classes='shrink-0 transition duration-300 group-open:-rotate-180'):
                            with FontAwesomeIcon(label="faChevronDown"):
                                pass

                        

                    with PD.Ul(classes='mt-3 flex-1 space-y-3') as ul_box:
                        pass

        def add_flat_item(key, label, ul_box=ul_box, **kwargs):
            with MuCtx:
                with Li(classes="justify-center px-4") as li_box:
                    with Button(key=key, classes='rounded-lg border border-2 border-indigo-500/50 px-4 py-1 text-sm font-medium text-indigo-500 uppercase leading-normal hover:bg-gradient-to-bl hover:from-gray-200 hover:to-gray-200 hover:via-gray-100/50 w-52 overflow-x-auto shadow shadow-indigo-200  hover:shadow-md hower:shadow-indigo-300', text=label, **kwargs):
                                pass

            ul_box.components.append(li_box)
        menu_box.components.append(group_box)
        group_box.add_flat_item = add_flat_item
        return group_box

    
                    
    def add_flat_item(key,
                      label,
                      menu_box=menu_box,
                      **kwargs):
        with MuCtx:
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
    comp_box.add_group_item = add_group_item
    return comp_box
