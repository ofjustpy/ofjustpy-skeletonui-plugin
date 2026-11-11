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
skui_comp_label = "accordion"


class AccordionMixin:

    def __init__(self, **kwargs):
        self.domDict.vue_type = "skeletonui_component"
        self.domDict.html_tag = "accordion_root"

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
_Accordion = ActiveDiv_StubWrappedTypeGen(
    "Accordion",
    AccordionMixin,
    stytags_getter_func=lambda m=ui_styles: m.sty.skui_accordion_root,
)

# Module-level component definitions
Root = CSR_comp_generator(_Accordion)


class AccordionItemMixin:
    valid_accordion_item_keys = [
        # "element" #TODO
        "value",
        "disabled",
    ]

    def __init__(self, **kwargs):
        assert "value" in kwargs

        for key in AccordionItemMixin.valid_accordion_item_keys:
            if key in kwargs:
                self.attrs[key] = kwargs[key]



# Sub-component using your strict addon_mixins specification
Item = gen_PassiveDiv_type_by_tag(
    "Item", prefix="Accordion_", addon_mixins=[AccordionItemMixin]
)

ItemTrigger = gen_PassiveDiv_type_by_tag("ItemTrigger", prefix="Accordion_")
ItemIndicator = gen_PassiveDiv_type_by_tag("ItemIndicator", prefix="Accordion_")
ItemContent = gen_PassiveDiv_type_by_tag("ItemContent", prefix="Accordion_")



Root = Root
Item = Item


import_stmt = """import { Accordion } from "@skeletonlabs/skeleton-svelte";
"""

# Module-level registry mapping
kv_label_to_shadcn_comp_map = """
    'accordion_root': Accordion,
    'accordion_item': Accordion.Item,
    'accordion_itemtrigger': Accordion.ItemTrigger,
    'accordion_itemindicator': Accordion.ItemIndicator,
    'accordion_itemcontent': Accordion.ItemContent,
"""


