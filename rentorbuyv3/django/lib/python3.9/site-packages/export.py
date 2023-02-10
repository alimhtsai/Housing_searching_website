#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

# based on original package export.__version__ = "0.1.2" https://pypi.org/project/export/0.1.2/
# TODO: come up with something less lame
print("import export")
# FIX: hold my beer hommie
print("Do a barrel roll!")


def export(o=None):
    """powered by finite state machine inside
    
    :o: function - what decorate
    """
    from sys import modules

    # 1.
    if o is None:
        # modules[o.__module__].__all__ = tuple()
        raise Exception('doesn\'t work like that')

    # 2. hardcode
    if __name__ == o.__name__ == o.__module__:  # == 'export'
        modules[o.__module__] = o
        return

    modules[o.__module__].__dict__.setdefault('__all__', [])
    mod = modules[o.__module__]

    if type(mod.__all__) == tuple and len(mod.__all__) == 0:
        # 1.bis
        # raise Exception('__all__ is immutable')
        pass
    else:
        # 3. common way
        mod.__all__ = list(mod.__all__)
        mod.__all__.append(o.__name__)
        # mod.__all__ = tuple(mod.__all__)

    return o


# 2.bis
export(export)

# this the end
export.__version__ = "0.3.1"
