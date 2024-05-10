import ofjustpy as oj
import skeletonui_components as SKUI
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

oj.set_style("un")
step1 = SKUI.Step(childs = [oj.PD.Prose(text="This example Stepper will teach you how to use this component. Tap")
                           ]
                 )
step1.set_slot_header(oj.PD.Prose(text="Get Started!"))

step2 = SKUI.Step(childs = [oj.PD.Prose(text="The steps will expand to fit content of any length."),
                            oj.PD.Prose(text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque vel expedita porro vero, saepe dicta repellendus facilis ab accusamus unde, tempora ut nobis eum. Veniam, architecto corrupti. Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque velexpedita porro vero, saepe dicta repellendus facilis ab accusamus unde, tempora ut nobis eum. Veniam, architecto corrupti. Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque vel expedita porro vero, saepe dicta repellendus facilis ab accusamus unde, tempora ut nobis eum. Veniam, architecto corrupti. Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque vel expedita porro vero, saepe dicta repellendus facilis ab accusamus unde, tempora ut nobis eum. Veniam, architecto corrupti. Lorem ipsum dolor sit amet consectetur adipisicing elit. Itaque vel expedita porro vero, saepe dicta repellendus facilis ab accusamus unde, tempora ut nobis eum. Veniam, architecto corrupti.")
                            ]
                  )
step2.set_slot_header(oj.PD.Prose(text="Long Form Content."))


step3 = SKUI.Step(childs = [oj.PD.Prose(text="A Complete button will appear on the last step. When the step is unlocked and the button pressed,")
                           ]
                 )
step3.set_slot_header(oj.PD.Prose(text="Almost Done."))

stepper = SKUI.Stepper(childs = [step1, step2, step3])


stepper_box= oj.PD.Div(childs=[stepper], extra_classes="w-full card p-4 text-token")

app = oj.load_app()
wp_endpoint = oj.create_endpoint(key="listbox",
                                 childs = [ stepper_box
                                     
                                           ],
                                 
                                 title="ListBox Demo"
                                 )
oj.add_jproute("/", wp_endpoint)
                

