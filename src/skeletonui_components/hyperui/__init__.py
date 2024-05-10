import ofjustpy as oj
from html_writer.macro_module import macros, writer_ctx

# ========================= select component =========================
def Base(key, title, on_change, **kwargs):
    with writer_ctx:
        with Div(classes="w-full flex justify-center"):
            
            with Div(extra_classes="card m-4",
                     **kwargs) as comp_box:
                with Label(for_='HeadlineAct',
                           extra_classes="flex justify-center block",
                           text=title):
                    pass

                with Select(key=key,
                            classes="",
                            extra_classes="variant-filled",
                            on_change=on_change) as select_box:
                    with Option(value='',
                                text='Please select',
                                extra_classes="variant-filled-primary"):
                        pass

    def add_option(value, text, select_box=select_box):
        with writer_ctx:
            with Option(value=value,
                        text=text,
                        extra_classes="card variant-filled-primary") as opt_item:
                    pass

        select_box.components.append(opt_item)

    comp_box.add_option = add_option
    return comp_box

# ====================== select -- list by group =====================
def BaseGroup(key, title, on_change, **kwargs):
    with writer_ctx:
        with Div(extra_classes="card variant-soft-primary",
                 **kwargs) as comp_box:
            with Label(for_=title,
                       extra_classes="block variant-filled-primary",
                       classes='',
                       text=title):
                pass

            with Select(key=key, classes='',
                        extra_classes="variant-soft-primary",
                        on_change=on_change) as select_box:
                with Option(value='',
                            text='Please select',
                            extra_classes="variant-filled-primary"
                            ):
                    pass

    def add_optgroup(label, select_box=select_box):
        with writer_ctx:
            with Optgroup(label=label, extra_classes="variant-soft-secondary") as optgroup_box:
                pass
        
        def add_option(value, text, optgroup_box=optgroup_box):
            with writer_ctx:
                with Option(value=value,
                            text=text,
                            extra_classes="variant-filled-primary"
                            ) as opt_item:
                        pass

            optgroup_box.components.append(opt_item)

        optgroup_box.add_option = add_option
        select_box.components.append(optgroup_box)
        return optgroup_box
    comp_box.add_optgroup = add_optgroup
    return comp_box

from . import sideMenu
from .buttons import  wideWithIcon as button_wideWithIcon
from .alerts import Popup
