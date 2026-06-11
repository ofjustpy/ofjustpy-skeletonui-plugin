import kavya as kv
from kavya.dsl import macros, MuCtx

circle_check_icon = kv.PC.FontAwesomeIcon(
                                 label="faCircleCheck", size="1x", 
                                 fixedWidth=True,
                            fa_group="regular"
                    )

times_circle_icon = kv.PC.FontAwesomeIcon(
                                 label="faCircleXmark",
                            size="1x", 
                                 fixedWidth=True,
                                 fa_group="regular"
                                 )


def Popup(key, title='', desc=''):
    with MuCtx:
        with Div(role='alert', classes='rounded-xl p-4', extra_classes="card variant-filled-primary") as comp_box:
            with Div(classes='flex items-start gap-4'):
                with Span(classes=''):
                    with ChildComp(child = circle_check_icon):
                        pass

                    pass
                with Div(classes='flex-1'):
                    with Strong(classes='block', text=f'{title}'):
                        pass

                    with P(classes='mt-1 text-sm ', text=f'{desc}'):
                        pass

                with Button(key=f"cross_{key}", classes='transition'):
                    with Span(classes='sr-only', text='Dismiss popup'):
                        pass

                    with ChildComp(child=times_circle_icon):
                        pass
                pass
            pass
        pass
    # with MuCtx:
    #     with Div(role='alert', classes='rounded-xl p-4', extra_classes="card variant-filled-primary") as comp_box:
    #         with Div(classes='flex items-start gap-4'):
    #             with Span(classes=''):
    #                 with kv.PC.FontAwesomeIcon(
    #                              label="faCircleCheck", size="1x", 
    #                              fixedWidth=True,
    #                         fa_group="regular"
    #                 ):
    #                     pass


    #             with Div(classes='flex-1'):
    #                 with Strong(classes='block', text=f'{title}'):
    #                     pass

    #                 with P(classes='mt-1 text-sm ', text=f'{desc}'):
    #                     pass

    #             with Button(key=f"cross_{key}", classes='transition'):
    #                 with Span(classes='sr-only', text='Dismiss popup'):
    #                     pass

    #                 with kv.PC.FontAwesomeIcon(
    #                              label="faTimesCircle",
    #                         size="1x", 
    #                              fixedWidth=True,
    #                              fa_group="regular"
    #                              ):
    #                     pass

    return comp_box
