default: fmt lint test

fmt:
    black .

ruff:
    ruff .

mypy:
    mypy --ignore-missing-imports .

lint: mypy ruff

test:
    pytest
