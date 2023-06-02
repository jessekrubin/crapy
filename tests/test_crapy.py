import io
import json

import crapy as cr


def test_print() -> None:
    string = json.dumps(list(range(100)))
    sio = io.StringIO()
    cr.print(string, file=sio)
    sio.seek(0)
    assert sio.read() == string + "\n"
