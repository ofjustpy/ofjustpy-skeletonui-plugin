import ofjustpy as oj
from py_tailwind_utils import *
from html_writer.macro_module import macros, writer_ctx

def wideWithIcon(href="#", text="", **kwargs):
    """
    childs, twsty_tags, and other attributes will be ignored
    """
    with writer_ctx:
        with A(classes="group flex items-center justify-between gap-4 rounded-lg px-5 py-3 transition-colors  focus:outline-none focus:ring", extra_classes="bg-primary-200 bg-opacity-20 text-primary-700 focus:shadow-ring-focus hover:bg-primary-400 hover:text-primary-600 focus:bg-primary-300 focus:text-primary-600", href=href) as button_box:
            with Span(extra_classes="font-medium transition-colors group-hover:text-secondary-600", text=text):

                pass

            with Span(extra_classes="shrink-0 rounded-full  group-active:border-secondary-500"):
                with FontAwesomeIcon(label="faExternalLinkAlt",
                                     size="1x", 
                                     fixedWidth=True,
                                     mdi_label="open-in-new"
                                     ):
                    pass

                pass

    return button_box
