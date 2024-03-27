import ofjustpy as oj
from html_writer.macro_module import macros, writer_ctx


def Base(key, title, on_change):
    with writer_ctx:
        with Div(extra_classes="variant-soft p-4") as comp_box:
            with Label(for_='HeadlineAct', extra_classes="variant-soft",
                       classes='block text-sm font-medium text-gray-900', text=title):
                pass

            with Select(key=key, extra_classes="variant-soft", on_change=on_change) as select_box:
                with Option(value='', text='Please select'):
                    pass

    def add_option(value, text, select_box=select_box):
        with writer_ctx:
            with Option(value=value, text=text, extra_classes="variant-filled") as opt_item:
                    pass

        select_box.components.append(opt_item)

    comp_box.add_option = add_option
    return comp_box


def BaseGroup(key, title, on_change):
    with writer_ctx:
        with Div(extra_classes="variant-soft p-4") as comp_box:
            with Label(for_=title, extra_classes="variant-soft", classes='block', text=title):
                pass

            with Select(key=key, classes='mt-1.5 p-2 w-full',
                        extra_classes="variant-soft",
                        on_change=on_change) as select_box:
                with Option(value='', text='Please select'):
                    pass

    def add_optgroup(label, select_box=select_box):
        with writer_ctx:
            with Optgroup(label=label) as optgroup_box:
                pass
        
        def add_option(value, text, optgroup_box=optgroup_box):
            with writer_ctx:
                with Option(value=value, text=text) as opt_item:
                        pass

            optgroup_box.components.append(opt_item)

        optgroup_box.add_option = add_option
        select_box.components.append(optgroup_box)
        return optgroup_box
    comp_box.add_optgroup = add_optgroup
    return comp_box
