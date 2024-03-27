import ofjustpy as oj
from py_tailwind_utils import *
import theme_select_bar 
from html_writer.macro_module import macros, writer_ctx


app = oj.load_app()
oj.set_style("un")


with writer_ctx:
    with HCCMutable_Div(key="tlbox", classes = "w-full grid grid-cols-1 md:grid-cols-2 gap-4",
             extra_classes="text-token") as card_box:
        with Mutable_Div(key="card_left", extra_classes="card variant-filled", classes="p-4 flex justify-center items-center") as card_left:
            with Span(text="Minimal"):
                pass

        with Mutable_Div(key="card_right", extra_classes="card variant-filled card-hover", classes="overflow-hidden") as card_right:
            with Header():
                with Img(src="https://images.unsplash.com/photo-1605106702734-205df224ecce?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80", alt = "", classes="w-full", extra_classes="aspect-[21/9] bg-black/50"):
                    pass
                pass
            with Div(classes="p-4, space-y-4"):
                with H6(text="Announcements"):
                    pass
                with H3(text="Skeleton is Awesome"):
                    pass
                with Article():
                    with Prose(text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Numquam aspernatur provident eveniet eligendi cumque consequatur temporesint nisi sapiente. Iste beatae laboriosam iure molestias cum expedita architecto itaque quae rem."):
                        pass
            with Hr(classes="opacity-50"):
                pass
            with Footer(classes="p-4 flex justify-start items-center space-x-4"):
                #needs avatar
                with Div(classes="flex-auto flex justify-between items-center"):
                    with H6(classes="font-bold", text="By Alex"):
                        pass
                    with Small(text="On 3/16/2024"):
                        pass

                    pass

                pass



def variant_selector(dbref, msg, to_ms):
    print("in variant_selector")
    print(msg.value)
    card_left_ms = to_ms(card_left)
    card_left_ms.update_extra_classes(f"card {msg.value}")
    card_right_ms = to_ms(card_right)
    card_right_ms.update_extra_classes(f"card {msg.value} card-hover")

theme_select_bar.on_change_variant_callback = variant_selector    
tlc = oj.HCCMutable.Container(childs = [card_box
                                ]
                      
                      )

wp_endpoint = oj.create_endpoint(key="",
                                 childs = [theme_select_bar.top_bar, oj.PD.Br(twsty_tags= [mr/st/4, W/full, H/4, mr/sb/4]),
                                           tlc

                                           ],
                                 
                                 title="Cards"
                                 )


oj.add_jproute("/", wp_endpoint)
