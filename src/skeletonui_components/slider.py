from kavya.session_managment.uictx_id_assigner import assign_id, id_assigner
from kavya.type_factory.static_type_factory import ActiveDiv_StubWrappedTypeGen, PassiveDiv_StubWrappedTypeGen
from kavya.htmlcomponents import html_tag_mixins as HTM
from kavya.themes import ui_styles


from .skeleton_type_factory import (
    gen_ActiveDiv_type_by_tag,
    gen_PassiveDiv_type_by_tag,
    CSR_comp_generator,
)
from kavya.themes import ui_styles

vue_type = "skeletonui_component"
skui_comp_label = "slider"


class SliderMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "skeletonui_component"
        self.domDict.html_tag = "slider_root"

        valid_accordion_keys = [
            # "animationConfig",
            # "base",
            # "padding",
            # "spaceY",
            # "rounded",
            # "width",
            # "classes",
            # "ids",
            # "multiple",
            # "collapsible",
            # "value",
            # "defaultValue",
            # "disabled",
            # "dir",
        ]

        for key in valid_accordion_keys:
            if key in kwargs:
                self.attrs[key] = kwargs[key]


# Base generation pipeline wrapper using ActiveDiv to track dynamic state changes
_Slider = ActiveDiv_StubWrappedTypeGen(
    "Slider",
    SliderMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.skui_slider_root,
)

# Module-level component definitions
Root = CSR_comp_generator(_Slider)


# class AccordionItemMixin:
#     valid_accordion_item_keys = [
#         # "element" #TODO
#         "value",
#         "disabled",
#     ]

#     def __init__(self, **kwargs):
#         assert "value" in kwargs

#         for key in AccordionItemMixin.valid_accordion_item_keys:
#             if key in kwargs:
#                 self.attrs[key] = kwargs[key]



# # Sub-component using your strict addon_mixins specification
# Item = gen_PassiveDiv_type_by_tag(
#     "Item", prefix="Accordion_", addon_mixins=[AccordionItemMixin]
# )

Label = gen_PassiveDiv_type_by_tag("Label", prefix="Slider_")
Control = gen_PassiveDiv_type_by_tag("Control", prefix="Slider_")
Track = gen_PassiveDiv_type_by_tag("Track", prefix="Slider_")
Range = gen_PassiveDiv_type_by_tag("Range", prefix="Slider_")
Thumb = gen_PassiveDiv_type_by_tag("Thumb", prefix="Slider_")
HiddenInput = gen_PassiveDiv_type_by_tag("HiddenInput", prefix="Slider_")
MarkerGroup = gen_PassiveDiv_type_by_tag("MarkerGroup", prefix="Slider_")
Marker = gen_PassiveDiv_type_by_tag("Marker", prefix="Slider_")






import_stmt = """import { Slider } from "@skeletonlabs/skeleton-svelte";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """
    'slider_root': Slider,
    'slider_label' : Slider.Label,
    'slider_control': Slider.Control,
    'slider_track' : Slider.Track,
    'slider_thumb' : Slider.Thumb,
    'slider_range' : Slider.Range,
    'slider_hiddeninput': Slider.HiddenInput,
    'slider_markergroup' : Slider.MarkerGroup,
    'slider_marker' : Slider.Marker
"""


