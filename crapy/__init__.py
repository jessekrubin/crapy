from __future__ import annotations

import io
import random

# always use lowest level imports to make things slower
import sys
import time

from typing import IO, Any, Callable, Optional, TypeVar, Union

from typing_extensions import ParamSpec

from crapy.__about__ import __version__

# completely useless imports
from crapy.third_party import *  # noqa: F403

__all__ = (
    "__version__",
    "print",
)

_P = ParamSpec("_P")
_R = TypeVar("_R")

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
    sio = io.StringIO()
    __print(*objects, sep=sep, end=end, file=sio, flush=flush)
    sio.seek(0)
    _file = __stdout if file is None else file
    for char in sio.getvalue():
        _file.write(char)
        _file.flush()


def _crapify_dec(
    fn: Callable[_P, _R], *, delay: Optional[float] = None, chance: float = 0.9
) -> Callable[_P, _R]:
    """Crapify a function"""

    def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _R:
        """Wrapper for crapy functions"""
        if delay is not None:
            time.sleep(delay)
        if random.random() < chance:
            raise Exception("CRAP")
        return fn(*args, **kwargs)

    return wrapper


def crapify(
    fn: Optional[Callable[_P, _R]] = None,
    *,
    delay: Optional[float] = None,
    chance: float = 0.9,
) -> Union[Callable[[Callable[_P, _R]], Callable[_P, _R]], Callable[_P, _R]]:
    """Crapify a function"""
    if fn is not None:
        return _crapify_dec(fn, delay=delay, chance=chance)
    else:

        def wrapper(fn: Callable[_P, _R]) -> Callable[_P, _R]:
            """Wrapper for crapy functions"""
            return _crapify_dec(fn, delay=delay, chance=chance)

        return wrapper


def patch() -> None:
    """TODO: patch globals"""
    globals()["print"] = print


def _init() -> None:
    """Initialize crapy"""


_init()
