from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR

class AccordionMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "accordion"
        for key in ['autocollapse', 'width', 'spacing', 'disabled', 'padding', 'hover',
                    'rounded', 'caretOpen', 'caretClosed', 'regionControl', 'regionPanel',
                    'regionCaret', 'transitions', 'transitionIn', 'transitionInParams',
                    'transitionOut', 'transitionOutParams']:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)

    # Property definitions remain the same


Accordion = gen_Div_type(
        HCType.passive,
        "Accordion",
        AccordionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.accordion,
        )
    

class AccordionItemMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "accordionitem"
        for key in ['open', 'id', 'transitionIn', 'transitionInParams',
                    'transitionOut', 'transitionOutParams']:
            if key in kwargs:
                self.attrs[key] = kwargs[key]

    def set_slot_lead(self, *args):
        self.domDict.slot_lead_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_summary(self, *args):
        self.domDict.slot_summary_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_content(self, *args):
        self.domDict.slot_content_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass
    def set_slot_iconClosed(self, *args):
        self.domDict.slot_iconClosed_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_iconOpen(self, *args):
        self.domDict.slot_iconOpen_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass    
AccordionItem = gen_Div_type(
        HCType.passive,
        "AccordionItem",
        AccordionItemMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.accordionitem,
        )                




# class SvelteFragmentMixin:
#     def __init__(self, **kwargs):
#         self.domDict.vue_type= "skeleton_component"
#         self.domDict.html_tag = "sveltefragment"
#         self.attrs = {}
#         for key in ['open', 'id', 'transitionIn', 'transitionInParams',
#                     'transitionOut', 'transitionOutParams']:
#             if key in kwargs:
#                 self.attrs[key] = kwargs[key]

# AccordionItem = gen_Div_type(
#         HCType.passive,
#         "AccordionItem",
#         AccordionItemMixin,
#         stytags_getter_func=lambda m=ui_styles: m.sty.accordionitem,
#         )                

class TabGroupMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "tabgroup"
        self.attrs['justify'] = kwargs.get('justify', "justify-start")
        self.attrs['border'] = kwargs.get('border', "border-b border-surface-400-500-token")
        print("in tabgroup", kwargs)
        self.attrs['active'] = kwargs.get('active', "border-b-2 border-surface-900-50-token")
        self.attrs['hover'] = kwargs.get('hover', "hover:variant-soft")
        self.attrs['flex'] = kwargs.get('flex', "flex-none")
        self.attrs['padding'] = kwargs.get('padding', "px-4 py-2")
        self.attrs['rounded'] = kwargs.get('rounded', "rounded-tl-container-token rounded-tr-container-token")
        self.attrs['spacing'] = kwargs.get('spacing', "space-y-1")
        self.attrs['regionList'] = kwargs.get('regionList', "")
        self.attrs['regionPanel'] = kwargs.get('regionPanel', "")
        self.attrs['labelledby'] = kwargs.get('labelledby', "")
        self.attrs['panel'] = kwargs.get('panel', "")

TabGroup = gen_Div_type(
        HCType.passive,
        "TabGroup",
        TabGroupMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tabgroup,
        )                

class TabMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "tab"
        for key in ['group', 'name', 'value', 'title', 'controls', 'regionTab']:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)
        self.domDict.tab_value = kwargs.get('tab_value')
        

Tab = gen_Div_type(
        HCType.active,
        "Tab",
        TabMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tab,
    static_addon_mixins = [TR.HCTextMixin]  
        )                               

class SlideToggleMixin:
    def __init__(self, **kwargs):
        """
        Initialize the SlideToggleMixin with the provided keyword arguments.

        Args:
            name (str): Required. Set a unique name for the input.
            checked (bool): The checked state of the input element. Defaults to False.
            size ('sm' | 'md' | 'lg'): Sets the size of the component. Defaults to 'md'.
            background (str): Provide classes to set the inactive state background color. Defaults to 'bg-surface-400 dark:bg-surface-700'.
            active (str): Provide classes to set the active state background color. Defaults to 'bg-surface-900 dark:bg-surface-300'.
            border (str): Provide classes to set the border styles.
            rounded (str): Provide classes to set border radius styles. Defaults to 'rounded-full'.
            label (str): Provide a semantic label.
        """
        
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "slidetoggle"
        for key in ['name', 'checked', 'size', 'background', 'active', 'border', 'rounded', 'label']:
            if key in kwargs:
                self.attrs[key] = kwargs[key]

SlideToggle = gen_Div_type(
        HCType.active,
        "",
        SlideToggleMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.tab,
    static_addon_mixins = [TR.HCTextMixin]  
        )

from ofjustpy.htmlcomponents_impl import assign_id
SlideToggle = assign_id(SlideToggle)

class ListBoxMixin:
    def __init__(self, **kwargs):
        """
        Initialize the ListBoxMixin with the provided keyword arguments.

        Args:
            multiple (bool): Enable selection of multiple items. Defaults to False.
            disabled (bool): Disables selection of items. Defaults to False.
            spacing (str): Provide class to set the vertical spacing style. Defaults to 'space-y-1'.
            rounded (str): Provide classes to set the listbox box radius styles. Defaults to 'rounded-token'.
            active (str): Provide classes to set the listbox item active background styles. Defaults to 'variant-filled'.
            hover (str): Provide classes to set the listbox item hover background styles. Defaults to 'hover:variant-soft'.
            padding (str): Provide classes to set the listbox item padding styles. Defaults to 'px-4 py-2'.
            regionLead (str): Provide arbitrary classes to style the lead region. Defaults to None.
            regionDefault (str): Provide arbitrary classes to the default region. Defaults to None.
            regionTrail (str): Provide arbitrary classes to the trail region. Defaults to None.
            labelledby (str): Provide the ARIA labelledby value. Defaults to None.
        """
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "listbox"
        for key in [
            'multiple', 'disabled', 'spacing', 'rounded', 'active', 'hover',
            'padding', 'regionLead', 'regionDefault', 'regionTrail', 'labelledby'
        ]:
            if key in kwargs:
                self.attrs[key] = kwargs[key]

ListBox = gen_Div_type(
        HCType.passive,
        "ListBox",
    ListBoxMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.listbox
        )

class ListBoxItemMixin:
    def __init__(self, **kwargs):
        """
        Initialize the ListBoxItemMixin with the provided keyword arguments.

        Args:
            rounded (str): Provide classes to set the listbox item rounded styles. Defaults to 'rounded-token'.
            active (str): Provide classes to set the listbox item active background styles. Defaults to 'variant-filled'.
            hover (str): Provide classes to set the listbox item hover background styles. Defaults to 'hover:variant-soft'.
            padding (str): Provide classes to set the listbox item padding styles. Defaults to 'px-4 py-2'.
        """
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "listboxitem"
        for key in ['rounded', 'active', 'hover', 'padding']:
            if key in kwargs:
                self.attrs[key] = kwargs[key]

        if "value" in kwargs:
            self.domDict["value"] = kwargs.get("value")
    def set_slot_lead(self, *args):
        self.domDict.slot_lead_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass
ListBoxItem = gen_Div_type(
        HCType.passive,
        "ListBoxItem",
    ListBoxItemMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.listboxitem,
    static_addon_mixins = [TR.HCTextMixin]  
        )
