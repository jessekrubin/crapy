import io
import json

import crapy as cr


def test_print() -> None:
    string = json.dumps(list(range(100)))
    sio = io.StringIO()
    cr.print(string, file=sio)
    sio.seek(0)
    assert sio.read() == string + "\n"


def test_crapify_always_error() -> None:
    @cr.crapify(chance=0.0)  # type: ignore[arg-type]
    def f() -> None:
        pass

    try:
        f()
        raise AssertionError("Should have raised")
    except Exception:
        ...
