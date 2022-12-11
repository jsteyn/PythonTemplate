import pytest
import src.new_package as n


@pytest.mark.parametrize(
    "test, expected",
    [
        ([0, 1]), ([1, 2]), ([2, 3])
    ]
)
def test_add_one(test, expected):
    assert n.add_one(test) == expected


@pytest.mark.parametrize(
    "test, expected",
    [
        ([-40, -40])
    ]
)
def test_convert_fahrenheit_to_celsius(test, expected):
    assert n.convert_fahrenheit_to_celsius(test) == expected

@pytest.mark.parametrize(
    "test, expected",
    [
        ([-40, -40])
    ]
)
def test_convert_celsius_to_fahrenheit(test, expected):
    assert n.convert_celsius_to_fahrenheit(test) == expected
