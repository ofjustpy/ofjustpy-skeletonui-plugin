import ofjustpy as oj
from py_tailwind_utils import *
import theme_bar_wrapper
from html_writer.macro_module import macros, writer_ctx


app = oj.load_app()
oj.set_style("un")



achip = oj.Mutable.Span(key="achip", extra_classes="chip variant-filled", text="chip")
# achip_box = oj.HCCMutable.Div(key="achip_box", twsty_tags=[W/full],
#           childs = [oj.Halign(achip, content_type="mutable"
#                                  )
#                     ]
#           )

achip_box = oj.HCCMutable.Subsubsection("Chips",
          oj.Halign(achip, content_type="mutable"
                                 )
          
          )


# ========================= chip with actions ========================
# <button class="chip variant-soft hover:variant-filled" on:click={doSomething}>
# 	<span>(icon)</span>
# 	<span>Action</span>
# </button>

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
                                 

# action_chips_box = oj.HCCMutable.Div(key="action_chips_box", twsty_tags=[W/full],
#           childs = [oj.Halign(action_chips, content_type="mutable"
#                                  )
#                     ]
#           )
action_chips_box = oj.HCCMutable.Subsubsection("Action Chips",
          oj.Halign(action_chips, content_type="mutable"
                                 )
          
          )

# ========================= chips with state =========================

# <div class="flex justify-center space-x-2">
# 						{#each ['red', 'blue', 'green'] as c}
# 							<!-- prettier-ignore -->
# 							<button
# 								class="chip {color === c ? 'variant-filled' : 'variant-soft'}"
# 								on:click={() => { section(c); }}
# 								on:keypress
# 							>
# 								{#if color === c}<span><i class="fa-solid fa-check" /></span>{/if}
# 								<span>{c}</span>
# 							</button>
# 						{/each}
# 					</div>

def on_state_chip_click(dbref, msg, to_ms):
    stubStore = msg.page.session_manager.stubStore

    print("stubStore  = ", stubStore.keys())

    stubStore.blue_check.target.add_twsty_tags(noop/hidden)
    stubStore.red_check.target.add_twsty_tags(noop/hidden)
    stubStore.green_check.target.add_twsty_tags(noop/hidden)
    
    match dbref.value:
       case 'red':
           stubStore.red_check.target.remove_twsty_tags(noop/hidden)

           
           print ("red clicked")

       case 'blue':
           stubStore.blue_check.target.remove_twsty_tags(noop/hidden)
           print ("blue clicked")

       case 'green':
           stubStore.green_check.target.remove_twsty_tags(noop/hidden)
           print ("green clicked")                      
           
    
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
action_state_chips_box = oj.HCCMutable.Subsubsection("State-Action Chips",
          oj.Halign(action_state_chips, content_type="mutable"
                                 )
          
          )                                                                    
def variant_selector(dbref, msg, to_ms):
    achip_ms = to_ms(achip)
    achip_ms.update_extra_classes(f"chip {msg.value}")


    heart_chip_ms = to_ms(heart_chip)
    heart_chip_ms.update_extra_classes(f"{msg.value} hover:variant-filled")

    share_chip_ms = to_ms(share_chip)
    share_chip_ms.update_extra_classes(f"{msg.value} hover:variant-filled")

    red_chip_box_ms = to_ms(red_chip_box)
    red_chip_box_ms.update_extra_classes(f"chip {msg.value}")

    green_chip_box_ms = to_ms(green_chip_box)
    green_chip_box_ms.update_extra_classes(f"chip {msg.value}")

    blue_chip_box_ms = to_ms(blue_chip_box)
    blue_chip_box_ms.update_extra_classes(f"chip {msg.value}")
    
top_bar = theme_bar_wrapper.get_top_bar()
theme_bar_wrapper.set_variant_selector(variant_selector)


tlc = oj.HCCMutable.Container(key="container", childs = [achip_box,
                                                         action_chips_box,
                                                         action_state_chips_box
                                                         ],
                              twsty_tags=[space/y/6]
                      
                      )

wp_endpoint = oj.create_endpoint(key="chips",
                                 childs = [top_bar, oj.PD.Br(twsty_tags= [mr/st/4, W/full, H/4, mr/sb/4]),
                                           tlc

                                           ],
                                 
                                 title="Chips"
                                 )
oj.add_jproute("/", wp_endpoint)
