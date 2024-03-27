from html_writer.macro_module import macros, writer_ctx
from skeletonui_components import *
from py_tailwind_utils import *
import ofjustpy as oj
app = oj.load_app()
print(tstr(badge))

# ============================== alerts ==============================
oj.set_style("un")

with writer_ctx:
    with Aside(extra_classes = "alert variant-ghost") as alert_box:
        with Div():
            with Span("Please put a font awesome icon here"):
                pass
            with Div(extra_class="alert-message"):
                with H3(text="ALter title"):
                    pass
                with Prose(text="alter message"):
                    pass
                with Div(extra_classes="alert-actions"):
                    with Button(key="alert_button", extra_classes="btn variant-filled", text="Action"):
                        pass
            
endpoint = oj.create_endpoint(key="td_skeleton_ui",
                   childs = [alert_box,
                             oj.PC.Span(text="hello", twsty_tags=[badge], extra_classes="variant-filled")],
                              data_theme= 'data-theme="skeleton"',
                   title = "skeleton ui"
                   )

                   
oj.add_jproute("/", endpoint)
