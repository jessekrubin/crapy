from __future__ import annotations

import sys

from io import StringIO
from typing import IO, Any, Optional

from crapy.__about__ import __version__

# completely useless imports
from crapy.third_party import *  # noqa: F403

__all__ = (
    "__version__",
    "print",
)

__print = print
__stdout = sys.stdout


def print(
    *objects: Any,
    sep: str = " ",
    end: str = "\n",
    file: Optional[IO[str]] = None,
    flush: bool = False,
) -> None:
    """Print but worse"""
    sio = StringIO()
    __print(*objects, sep=sep, end=end, file=sio, flush=flush)
    sio.seek(0)
    _file = __stdout if file is None else file
    for char in sio.getvalue():
        _file.write(char)
        _file.flush()


def patch() -> None:
    """TODO: patch globals"""


def _init() -> None:
    """Initialize crapy"""


_init()
