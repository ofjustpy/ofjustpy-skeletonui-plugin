from ofjustpy.Div_TF import gen_Div_type
from ofjustpy_engine.HCType import HCType
from ofjustpy import ui_styles
from ofjustpy_engine import HC_Div_type_mixins as TR
from ofjustpy.htmlcomponents_impl import assign_id
from ofjustpy.icons import FontAwesomeIcon

class AccordionMixin:
    """
    Provides the attributes for a Skeleton Svelte Accordion component.

    Ref: https://www.skeleton.dev/components/accordions (Adjust URL if needed)

    Note:
        - Content (children) is added by nesting AccordionItem components within this component.
        - Icons (iconOpen, iconClosed) are typically handled within AccordionItem, not set globally here.
        - Event callbacks (onValueChange, onFocusChange) are handled via the component's event system (e.g., using `.on('valueChange', handler)`).
        - Use `value` for controlled state or `defaultValue` for uncontrolled initial state.
    """
    def __init__(self, **kwargs):
        self.domDict['vue_type'] = "skeleton_component"
        self.domDict['html_tag'] = "accordion"
        # Ensure attrs dictionary exists if not already initialized

        # List of valid Accordion props to be passed directly as attributes
        # Excludes slots (children, iconOpen, iconClosed) and events (onValueChange, etc.)
        valid_accordion_keys = [
            'animationConfig',  # dict: The animation configuration
            'base',             # str: Sets base styles
            'padding',          # str: Set padding styles
            'spaceY',           # str: Set vertical spacing styles
            'rounded',          # str: Set border radius styles
            'width',            # str: Set the width styles
            'classes',          # str: Provide arbitrary CSS classes
            'ids',              # dict: Ids of elements, useful for composition
            'multiple',         # bool: Allow multiple items open (default: False)
            'collapsible',      # bool: Allow closing expanded items (default: False)
            'value',            # str | list[str]: Controlled value (expanded items)
            'defaultValue',     # str | list[str]: Initial value (uncontrolled)
            'disabled',         # bool: Disable all items (default: False)
            'dir',              # str: Text direction "ltr" | "rtl" (default: "ltr")
            # 'getRootNode' - Advanced, usually not set via simple props
        ]

        for key in valid_accordion_keys:
            if key in kwargs:
                # Copy the value from kwargs to the component's attributes
                self.attrs[key] = kwargs[key]



        


Accordion = gen_Div_type(
        HCType.passive,
        "Accordion",
        AccordionMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.accordion,
        )
    

class AccordionItemMixin:
    valid_accordion_item_keys = [
            'headingLevel',     # number: The heading level for the control element.
            'base',             # str: Sets base styles for the item's root element.
            'spaceY',           # str: Set vertical spacing styles. (Less common on item vs parent?)
            'classes',          # str: Provide arbitrary CSS classes to the item's root element.

            # Control (Button/Header) Styling
            'controlBase',      # str: Sets control's base styles.
            'controlHover',     # str: Sets control's the hover styles.
            'controlPadding',   # str: Sets control's the padding styles.
            'controlRounded',   # str: Sets control's the border radius styles.
            'controlClasses',   # str: Provide arbitrary CSS classes to the control.

            # Lead (Icon/Element before control text) Styling
            'leadBase',         # str: Sets the lead's base styles.
            'leadClasses',      # str: Provide arbitrary CSS classes to the lead.

            # Content/Panel Styling (Note: API description typo likely means 'content' not 'lead')
            'contentBase',      # str: Sets the content/panel's base styles.
            'contentClasses',   # str: Provide arbitrary CSS classes to the content/panel.

            # Indicator (Icon/Caret) Styling (Note: API description typo likely means 'indicator' not 'lead')
            'indicatorBase',    # str: Sets the indicator's base styles.
            'indicatorClasses', # str: Provide arbitrary CSS classes to the indicator.

            # Panel (Collapsible Content Area) Styling
            'panelBase',        # str: Set the panel's base styles.
            'panelPadding',     # str: Set the panel's padding styles.
            'panelRounded',     # str: Set the panel's border-radius styles.
            'panelClasses',     # str: Provide arbitrary CSS classes to the panel.

            # Core Properties
            'value',            # str: *Required* The unique value of the accordion item.
            'disabled',         # bool: Whether the accordion item is disabled.
        ]

    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "accordionitem"
        assert 'value' in kwargs

        for key in AccordionItemMixin.valid_accordion_item_keys:
            if key in kwargs:
                # Copy the value from kwargs to the component's attributes
                self.attrs[key] = kwargs[key]
                


    def set_slot_lead(self, *args):
        self.domDict.slot_lead_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_control(self, *args):
        self.domDict.slot_control_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_content(self, *args):
        self.domDict.slot_panel_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass
    # def set_slot_iconClosed(self, *args):
    #     self.domDict.slot_iconClosed_json = [_.convert_object_to_jsondict() for _ in args]
        
    #     pass

    # def set_slot_iconOpen(self, *args):
    #     self.domDict.slot_iconOpen_json = [_.convert_object_to_jsondict() for _ in args]
        
    #     pass    
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

class TabsMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "tabs"

        self.domDict.slot_list_json = []
        self.domDict.slot_panel_json = []
        for key in  ["fluid",
                     "base",
                     "classes",
                     "listBase",
                     "listJustify",
                     "listBorder",
                     "listMargin",
                     "listGap",
                     "listClasses",
                     "contentBase",
                     "contentClasses",
                     "ids",
                    "value",
                    "defaultValue",
                    "dir",
                    "loopFocus",
                    "translations",
                    "composite",
                    "activationMode",
                    "deselectable"
                     ]:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)

            
    def set_slot_list(self, *args):
        self.domDict.slot_list_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass
    
    def set_slot_content(self, *args):
        self.domDict.slot_content_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

     
Tabs  = gen_Div_type(
        HCType.passive,
        "Tabs",
        TabsMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.skui_tabs,
        )



class TabsControlMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "tabscontrol"
        for key in ["base",
                    "padding",
                    "translateX",
                    "classes",
                    "labelBase",
                    "labelClasses",
                    "stateInactive",
                    "stateActive",
                    "stateLabelInactive",
                    "stateLabelActive",
                    "value",
                    "disabled"
                    ]:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)

TabsControl  = gen_Div_type(
        HCType.passive,
        "TabsControl",
        TabsControlMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.skui_tabscontrol,
        static_addon_mixins = [TR.HCTextMixin]  
        )


class TabsPanelMixin:
    def __init__(self, **kwargs):
        self.domDict.vue_type= "skeleton_component"
        self.domDict.html_tag = "tabspanel"
        for key in ["base", "classes", "value"
                    ]:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)

TabsPanel  = gen_Div_type(
        HCType.passive,
        "TabsPanel",
        TabsPanelMixin,
        stytags_getter_func=lambda m=ui_styles: m.sty.skui_tabspanel,
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


class RatingsMixin:
    def __init__(self, **kwargs):
        """
        Initialize RatingsMixin with the provided attributes.

        Args:
        - value (number, optional): Current rating value. Default is 0.
        - max (number, optional): Maximum rating value. Default is 5.
        - interactive (boolean, optional): Enables interactive mode for each rating icon. Default is False.
        - text (string, optional): Provide classes to set the text color. Default is 'text-token'.
        - fill (string, optional): Provide classes to set the SVG fill color. Default is 'fill-token'.
        - justify (string, optional): Provide classes to set the flexbox justification. Default is 'justify-center'.
        - spacing (string, optional): Provide classes to set the horizontal spacing style. Default is 'space-x-2'.
        - regionIcon (string, optional): Provide arbitrary classes to the icon region. Default is None.
        """
        self.domDict['vue_type'] = "skeleton_component"
        self.domDict['html_tag'] = "ratings"
        
        for key in ['value', 'max', 'interactive', 'text', 'fill', 'justify',
                    'spacing', 'regionIcon']:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)

        self.domDict.slot_empty_json = [_.convert_object_to_jsondict() for _ in [FontAwesomeIcon(label="faStarHalfStroke", size="1x")

                                                                                 ]
                                        ]
        
        self.domDict.slot_half_json = [_.convert_object_to_jsondict() for _ in [FontAwesomeIcon(label="faStarHalfStroke", size="1x")

                                                                                ]
                                       
                                       ]
        self.domDict.slot_full_json = [_.convert_object_to_jsondict() for _ in [FontAwesomeIcon(label="faStar", size="1x")
                                                                                ]
                                       ]
        
    def set_slot_empty(self, *args):
        self.domDict.slot_empty_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

    def set_slot_half(self, *args):
        self.domDict.slot_half_json = [_.convert_object_to_jsondict() for _ in args]
            
        pass

    def set_slot_full(self, *args):
        self.domDict.slot_full_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass


Ratings = gen_Div_type(HCType.active,
                       "Ratings",
                       RatingsMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.skeletonui_ratings
                       )

Ratings = assign_id(Ratings)

# ============================== Stepper =============================
class StepperMixin:
    def __init__(self, *args, **kwargs):
        """
        Initialize StepperMixin with the provided attributes.

        Args:
        - jp_props_list (list): List of jp_props.object_props.
        - valueSingle (str): Current value for the stepper.
        - eventHandlers (dict): Dictionary containing event handlers, such as 'click'.
        - gap (string, optional): Provide classes to style the stepper header gap. Default is 'gap-4'.
        - stepTerm (string, optional): Provide the verbiage that represents "Step". Default is 'Step'.
        - badge (string, optional): Provide classes to style the stepper header badges. Default is 'variant-filled-surface'.
        - active (string, optional): Provide classes to style the stepper header active step badge. Default is 'variant-filled'.
        - border (string, optional): Provide classes to style the stepper header border. Default is 'border-surface-400-500-token'.
        - start (number, optional): Provide the initially selected step. Default is 0.
        - justify (string, optional): Set the justification for the step navigation buttons. Default is 'justify-between'.
        - buttonBack (string, optional): Provide arbitrary classes to style the back button. Default is 'variant-ghost'.
        - buttonBackType (string, optional): Set the type of the back button. Default is 'button'.
        - buttonBackLabel (string, optional): Provide the HTML label content for the back button. Default is '← Back'.
        - buttonNext (string, optional): Provide arbitrary classes to style the next button. Default is 'variant-filled'.
        - buttonNextType (string, optional): Set the type of the next button. Default is 'button'.
        - buttonNextLabel (string, optional): Provide the HTML label content for the next button. Default is 'Next →'.
        - buttonComplete (string, optional): Provide arbitrary classes to style the complete button. Default is 'variant-filled-primary'.
        - buttonCompleteType (string, optional): Set the type of the complete button. Default is 'button'.
        - buttonCompleteLabel (string, optional): Provide the HTML label content for the complete button. Default is 'Complete'.
        - regionHeader (string, optional): Provide arbitrary classes to the stepper header region. Default is None.
        - regionContent (string, optional): Provide arbitrary classes to the stepper content region. Default is None.
        - transitions (boolean, optional): Enable/Disable transitions. Default is !$prefersReducedMotionStore.
        - transitionIn (TransitionIn, optional): Provide the transition to used on entry. Default is None.
        - transitionInParams (TransitionParams, optional): Transition params provided to `transitionIn`. Default is { duration: 100 }.
        - transitionOut (TransitionOut, optional): Provide the transition to used on exit. Default is None.
        - transitionOutParams (TransitionParams, optional): Transition params provided to `transitionOut`. Default is { duration: 100 }.
        """
        self.domDict['vue_type'] = "skeleton_component"
        self.domDict['html_tag'] = "stepper"
        
        for key in [
            'gap', 'stepTerm', 'badge', 'active', 'border', 'start', 'justify',
            'buttonBack', 'buttonBackType', 'buttonBackLabel', 'buttonNext',
            'buttonNextType', 'buttonNextLabel', 'buttonComplete', 'buttonCompleteType',
            'buttonCompleteLabel', 'regionHeader', 'regionContent', 'transitions',
            'transitionIn', 'transitionInParams', 'transitionOut', 'transitionOutParams'
        ]:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)






Stepper = gen_Div_type(HCType.passive,
                       "Stepper",
                       StepperMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.skeletonui_stepper
                       )

class StepMixin:
    def __init__(self, *args, **kwargs):
        """
        Initialize StepMixin with the provided attributes.

        Args:
        - locked (boolean, optional): Flag to indicate if the step is locked. Default is False.
        - regionHeader (string, optional): Provide arbitrary classes to the step header region. Default is None.
        - regionContent (string, optional): Provide arbitrary classes to the step content region. Default is None.
        - regionNavigation (string, optional): Provide arbitrary classes to the step navigation region. Default is None.
        - transitionIn (TransitionIn, optional): Provide the transition to used on entry. Default is None.
        - transitionInParams (TransitionParams, optional): Transition params provided to `transitionIn`. Default is None.
        - transitionOut (TransitionOut, optional): Provide the transition to used on exit. Default is None.
        - transitionOutParams (TransitionParams, optional): Transition params provided to `transitionOut`. Default is None.
        """

        self.domDict['vue_type'] = "skeleton_component"
        self.domDict['html_tag'] = "step"
        
        for key in [
            'locked', 'regionHeader', 'regionContent', 'regionNavigation',
            'transitionIn', 'transitionInParams', 'transitionOut', 'transitionOutParams'
        ]:
            if key in kwargs:
                self.attrs[key] = kwargs.get(key)
    def set_slot_header(self, *args):
        self.domDict.slot_header_json = [_.convert_object_to_jsondict() for _ in args]
        
        pass

Step = gen_Div_type(HCType.passive,
                       "Step",
                       StepMixin,
                       stytags_getter_func=lambda m=ui_styles: m.sty.skeletonui_step
                       )
