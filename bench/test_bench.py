from typing import Any

import pytest
import pytest_benchmark

import crapy


@pytest.mark.benchmark(group="print")
@pytest.mark.parametrize(
    "printfn",
    [
        pytest.param(print, id="builtin"),
        pytest.param(crapy.print, id="crapy"),
    ],
)
def test_bench_print(
    printfn: Any, benchmark: pytest_benchmark.fixture.BenchmarkFixture
) -> None:
    benchmark(printfn, "howdy doody")
