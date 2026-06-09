"""
See https://www.skeleton.dev/docs/tailwind/forms
"""
import ofjustpy as oj
import demo_uisty

from html_writer.macro_module import macros, writer_ctx
from py_tailwind_utils import *
app = oj.load_app()

twsty_tags=[noop/select, bdr.container, mr/x/auto, W/full, max/W/md, space/y/4

]
print(tstr(*twsty_tags))
with oj.TwStyCtx(demo_uisty):

    with writer_ctx:
        with Active.Form(key="aform", twsty_tags=[mr/x/auto,
                                                  W/full,
                                                  max/W/md,
                                                  space/y/4,
                                                  flxdir.col
                                                  ]) as tlc:
        # Default
            with Active.Select(key="select1",
                               twsty_tags=[]
                               ):
                with Option(value="1",
                            text="Option 1"
                            ):
                    pass
                with Option(value="2", text="Option 2"):
                    pass
                with Option(value="3", text="Option 3"):
                    pass
                with Option(value="4", text="Option 4"):
                    pass
                with Option(value="5", text="Option 5"):
                    pass            


            with Active.Select(key="select2", twsty_tags=[bdr.container], size="4", value="1"):
                with Option(value="1", text="Option 1"):
                    pass
                with Option(value="2", text="Option 2"):
                    pass
                with Option(value="3", text="Option 3"):
                    pass
                with Option(value="4", text="Option 4"):
                    pass
                with Option(value="5", text="Option 5"):
                    pass

            with Active.Select(key="select3", twsty_tags=[bdr.container], multiple=True, value="['1', '2']"):
                with Option(value="1", text="Option 1"):
                    pass
                with Option(value="2", text="Option 2"):
                    pass
                with Option(value="3", text="Option 3"):
                    pass
                with Option(value="4", text="Option 4"):
                    pass
                with Option(value="5", text="Option 5"):
                    pass
            
endpoint = oj.create_endpoint("demo_forms",
                              childs = [tlc],
                              csr_bundle_dir="browser_bundle",
                              skeleton_data_theme="seafoam"                            
                              )


oj.add_jproute("/", endpoint)
        
