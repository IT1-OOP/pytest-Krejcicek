import pytest
from src import calculator

def test_add():
    assert calculator.add(1,2) == 3
    assert calculator.add(0,5) == 5
    assert calculator.add(-2,9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():
    assert calculator.add_wrong(1,2) == 3
    assert calculator.add_wrong(0,5) == 5
    assert calculator.add_wrong(-2,9) == 7
    assert calculator.add_wrong(0,0) == 0

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 5, 5), (-2, 9, 7), (5, -8, -3)],)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 5, 5), (-2, 9, 7), (5, -8, -3)],)
def test_add_wrong_parametrized(a,b, expected):
    assert calculator.add_wrong(a, b) == expected

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(0, 5) == -5
    assert calculator.subtract(-2, -7) == 5

@pytest.mark.parametrize("a, b, expected", [(5, 3, 2), (10, 5, 5), (0, 5, -5), (-2, -7, 5)],)
def test_subtract_parametrized(a, b, expected):
    assert calculator.subtract(a, b) == expected

def test_multiply():
    assert calculator.multiply(5, 3) == 15
    assert calculator.multiply(10, 5) == 50
    assert calculator.multiply(0, 5) == 0
    assert calculator.multiply(-2, -7) == 14

@pytest.mark.parametrize("a, b, expected", [(5, 3, 15), (10, 5, 50), (0, 5, 0), (-2, -7, 14)],)
def test_multiply_parametrized(a, b, expected):
    assert calculator.multiply(a, b) == expected

