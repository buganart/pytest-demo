import pytest

from my_pkg.code import sort


@pytest.fixture
def integers():
    return [3, 1, 2]


def test_sort_integers(integers):
    assert sort(integers) == [1, 2, 3]


@pytest.fixture(
    params=[
        "integers",
        "strings",
    ]
)
def items(request):
    if request.param == "integers":
        return [3, 1, 2]
    else:
        return ["b", "a", "c"]


def test_sort_strings(strings):
    assert sort(strings) == ["a", "b", "c"]


def test_examples(items):
    assert sort(items) == sorted(items)


@pytest.fixture
def objects(request):
    return request.param


@pytest.mark.parametrize(
    "objects",
    [
        [1.0, 3.0, 2.0],
    ],
    indirect=True,
)
def test_examples_parametrized(objects):
    assert sort(objects) == sorted(objects)


def test_fails_on_different_types():
    items = [1, "foo"]
    with pytest.raises(ValueError) as exc:
        # can check exception string
        sort(items)
