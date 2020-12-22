# Why test?
If all tests pass. The code "should" be correct.

# How to run tests

    pytest -v

    pytest path/to/file.py

# How to use file watcher (pytest-watch)

    ptw -- -v

# Test functions
Anything starting with `test_`.

# Test collection
Pytest finds all the tests.

    pytest --collect-only

# Fixtures
- Input to test functions.
- "Test data".

# Pytest test runner flags

- see output: no capture `-s`
- verbose `-v`
- re-run failed `--failed-first`
- filter by markers `-m`
- start debugger on errors `--pdb`
- show fixtures `--setup-show`

# Sharing fixtures
Put in `conftest.py` at same level of test file or in any parent (but still
inside test directory).

# Parametrized fixtures

1. `pytest.fixture(params=[1, 2])`
2. `@pytest.mark.parametrize("foo", [1, 2])`

Last part can also be used with `indirect=True`.

# Coverage
## Terminal report

    pytest --cov my_pkg

## HTML report

    pytest --cov my_pkg --cov-report html

Browse coverage in browser

    chromium htmlcov/index.html

## codecov.io
Can be checked for code that has been pushed to github.
