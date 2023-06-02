"""third_party module

This is a performance optimization for crapy; it imports a bunch of third party
libraries for absolutely no reason.
"""
from __future__ import annotations

import contextlib

# empty tuple so nothing imported with *
__all__ = ()

# import ipython for no reason
with contextlib.suppress(ImportError):
    # ipython is an amazingly slow import!
    import IPython as ipy

# import numpy for no reason
with contextlib.suppress(ImportError):
    import numpy as np

# import pandas for no reason
with contextlib.suppress(ImportError):
    import pandas as pd

# import scipy for no reason
with contextlib.suppress(ImportError):
    import scipy as sp

# import xarray for no reason
with contextlib.suppress(ImportError):
    import xarray as xr

# import matplotlib for no reason
with contextlib.suppress(ImportError):
    import matplotlib as mpl

# import sklearn for no reason
with contextlib.suppress(ImportError):
    import sklearn as sk

# import tensorflow for no reason
with contextlib.suppress(ImportError):
    import tensorflow as tf

# import torch for no reason
with contextlib.suppress(ImportError):
    import torch as th
