import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx

app = oj.load_app()
oj.set_style("un")

with writer_ctx:
    with Div(key="tlbox", classes = "w-full grid grid-cols-1 md:grid-cols-2 gap-4",
             extra_classes="text-token") as card_box:
        with Div(key="card_left",
                 extra_classes="card variant-filled",
                 classes="p-4 flex justify-center items-center") as card_left:
            with Span(text="Minimal"):
                pass

        with Div(key="card_right",
                         extra_classes="card variant-filled card-hover",
                         classes="overflow-hidden") as card_right:
            with Header():
                with Img(src="https://img.pikbest.com/wp/202343/bathroom-tile-vibrant-texture-of-a-mosaic-glass-wall-in-the_9973098.jpg!w700wp",
                         alt = "",
                         classes="w-full",
                         extra_classes="aspect-[21/9] bg-black/50"):

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


cards_box = oj.HCCStatic.Div(key="Cardsbox",
                              childs=[card_box],
                              extra_classes="variant-ghost-tertiary w-full card p-4"
                              )
