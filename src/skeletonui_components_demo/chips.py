import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx
app = oj.load_app()
oj.set_style("un")

achip = oj.Mutable.Span(key="achip",
                        extra_classes="chip variant-filled-primary",
                        text="chip"
                        )
achip_box = oj.HCCMutable.Subsection("Chips",
                                        oj.Halign(achip,
                                                  content_type="mutable"
                                                  ),
                                     section_depth=10
                                        )

async def on_chip_click(dbref, msg, to_ms):
    await msg.page.trigger_toast(dbref.value)
    
    pass


with writer_ctx:
    with HCCMutable_Div(key="ActionChips", classes="flex justify-center space-x-2") as action_chips:
        with Mutable_ButtonDiv(key="heart_chip", classes="p-2", extra_classes="variant-soft hover:variant-filled", value="like", on_click=on_chip_click) as heart_chip:
            with FontAwesomeIcon(label="faHeart", size="1x", 
                                 fixedWidth=True,
                                 ):
                pass

            with Span(text="Like"):
                pass
            
        with Mutable_ButtonDiv(key="share_chip", classes="p-2", extra_classes="variant-soft hover:variant-filled", value="share", on_click=on_chip_click) as share_chip:
            with FontAwesomeIcon(label="faShare", size="1x", 
                                 fixedWidth=True,

                                 ):
                pass

            with Span(text="Share"):
                pass    
                                 

action_chips_box = oj.HCCMutable.Subsection("Action Chips",
                                               oj.Halign(action_chips,
                                                         content_type="mutable"
                                                         ),
                                            section_depth=10
                                               
                                               )

def on_state_chip_click(dbref, msg, to_ms):
    stubStore = msg.page.session_manager.stubStore

    stubStore.blue_check.target.add_twsty_tags(noop/hidden)
    stubStore.red_check.target.add_twsty_tags(noop/hidden)
    stubStore.green_check.target.add_twsty_tags(noop/hidden)
    
    match dbref.value:
       case 'red':
           stubStore.red_check.target.remove_twsty_tags(noop/hidden)

       case 'blue':
           stubStore.blue_check.target.remove_twsty_tags(noop/hidden)

       case 'green':
           stubStore.green_check.target.remove_twsty_tags(noop/hidden)
    
    pass


with writer_ctx:
    with HCCMutable_Div(classes="flex justify-center space-x-2") as action_state_chips:
        with Mutable_ButtonDiv(key="red_chip", extra_classes="chip variant-filled", value="red",
                       on_click = on_state_chip_click
                       ) as red_chip_box:
            with Mutable_Div(key="red_check", twsty_tags=[noop/hidden]):
                with FontAwesomeIcon(label="faCheck", fixedWidth=True):
                    pass
            with Span(text='red'):
                pass

        with Mutable_ButtonDiv(key="blue_chip", extra_classes="chip variant-filled", value="blue",
                       on_click = on_state_chip_click
                       ) as blue_chip_box:
            with Mutable_Div(key="blue_check", twsty_tags=[noop/hidden]):
                with FontAwesomeIcon(label="faCheck", fixedWidth=True):
                    pass
            with Span(text='blue'):
                pass

        with Mutable_ButtonDiv(key="green_chip", extra_classes="chip variant-filled", value="green",
                       on_click = on_state_chip_click
                       ) as green_chip_box:
            with Mutable_Div(key="green_check", twsty_tags=[noop/hidden]):
                with FontAwesomeIcon(label="faCheck", fixedWidth=True):
                    pass
            with Span(text='green'):
                pass                        
            

action_state_chips_box = oj.HCCMutable.Div(key="action_state_chips_box", twsty_tags=[W/full],
          childs = [oj.Halign(action_state_chips, content_type="mutable"
                                 )
                    ]
          )            




chips_box = oj.Mutable.Div(key="Chipsbox",
                     childs = [achip_box,
                               action_chips_box,
                               action_state_chips_box
                               ],
                           extra_classes="variant-ghost-tertiary w-full card p-4 space-y-4 flex flex-col items-center"
                     )
