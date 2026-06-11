import kavya as kv
from py_tailwind_utils import *

class Button(kv.AC.Button):
    def __init__(self, **kwargs):
        # 1. Safely extract and merge the tags
        twsty_tags = kwargs.pop("twsty_tags", [])
        # 2. Ensure your component's core tag is prepended
        kwargs["twsty_tags"] = [noop/btn, *twsty_tags]
        
        # 3. Initialize the parent class properly
        super().__init__(**kwargs)


