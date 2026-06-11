import kavya as kv
from py_tailwind_utils import *

# class Button(kv.AD.Button):
#     def __init__(self, **kwargs):
#         # 1. Safely extract and merge the tags
#         twsty_tags = kwargs.pop("twsty_tags", [])
#         # 2. Ensure your component's core tag is prepended
#         kwargs["twsty_tags"] = [noop/btn, *twsty_tags]
        
#         # 3. Initialize the parent class properly
#         super().__init__(**kwargs)


class Title(kv.PD.Halign):
    def __init__(self, title_text, twsty_tags=None, align="center", **kwargs):
        if twsty_tags is None:
            twsty_tags = []
            
        # 1. Prep the inner Span component's tags
        merged_tags = [ptypo/title, *twsty_tags]
        
        # 2. Build the child Span node
        span_content = kv.PC.Span(
            text=title_text,
            twsty_tags=merged_tags,
            **kwargs,
        )
        
        # 3. Pass the child node up to the Halign parent container
        super().__init__(span_content, align=align)
        
