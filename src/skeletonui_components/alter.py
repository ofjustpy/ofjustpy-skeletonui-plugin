import sys
from aenum import Enum

from py_tailwind_utils.common import TagBase

class _badge(TagBase):
    tagstr = "badge"
    tagops = []
    taghelp = "badge"
    elabel = "badge"
    stemval = "badge"

badge = _badge()



class FilledVariant(Enum):
    _ = "variant-filled"
    
    surface = "variant-filled-surface"

    primary = "variant-filled-primary"


class _FilledVariant:
    _sv_class = FilledVariant

    @property
    def surface(cls):
        return noop / cls._sv_class.surface

    @property
    def primary(cls):
        return noop / cls._sv_class.primary

