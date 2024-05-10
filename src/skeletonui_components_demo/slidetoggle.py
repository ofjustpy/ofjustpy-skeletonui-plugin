import ofjustpy as oj
from skeletonui_components.components import SlideToggle
from py_tailwind_utils import *
from ofjustpy.icons import FontAwesomeIcon
from py_tailwind_utils import *

slidetoggle_styled_1 = SlideToggle(key="slidetoggle",
                                  checked=True,
                                  rounded="rounded-sm",
                                  size="sm",
                                  border="border-double",
                                  background="bg-surface-400",
                                  active="bg-surface-900",
                                  )

slidetoggle_styled_2 = SlideToggle(key="slidetoggle",
                                    checked=True,
                                    rounded="rounded-md",
                                    size="md",
                                    border="border-dotted"
                                    
                                    )

slidetoggle_styled_3 = SlideToggle(key="slidetoggle",
                                    checked=True,
                                    rounded="rounded-full",
                                    border="border-none",
                                    size="lg")

slidetoggle_box = oj.HCCStatic.Div(key="Slidetogglebox",
                                   childs=[slidetoggle_styled_1,
                                           slidetoggle_styled_2,
                                           slidetoggle_styled_3
                                           ],
                                   extra_classes="variant-ghost-tertiary w-full card p-4 space-y-4 flex flex-col items-center"
                              )
