import ofjustpy as oj
from ofjustpy import icons
from html_writer.macro_module import macros, writer_ctx

def Popup(key, title='', desc=''):
    with writer_ctx:
        with Div(role='alert', classes='rounded-xl p-4', extra_classes="card variant-filled-primary") as comp_box:
            with Div(classes='flex items-start gap-4'):
                with Span(classes=''):
                    with FontAwesomeIcon(
                                 label="faCircleCheck", size="1x", 
                                 fixedWidth=True,
                            fa_group="regular"
                    ):
                        pass


                with Div(classes='flex-1'):
                    with Strong(classes='block', text=f'{title}'):
                        pass

                    with P(classes='mt-1 text-sm ', text=f'{desc}'):
                        pass

                with Button(key=f"cross_{key}", classes='transition'):
                    with Span(classes='sr-only', text='Dismiss popup'):
                        pass

                    with FontAwesomeIcon(
                                 label="faTimesCircle",
                            size="1x", 
                                 fixedWidth=True,
                                 fa_group="regular"
                                 ):
                        pass

    return comp_box
