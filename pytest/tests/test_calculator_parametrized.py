import pytest
from src import calculator

def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(0, 5) == 5
    assert calculator.add(-2, 9) == 7
    assert calculator.add(5, -8) == -3

def test_add_2():  
    assert calculator.add(1, 2) == 3
    assert calculator.add(0, 5) == 5
    assert calculator.add(-2, 9) == 7
    assert calculator.add(5, -8) == -3

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 5, 5), (-2, 9, 7), (5, -8, -3)],)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (0, 5, 5), (-2, 8, 7), (6, -8, -3)],)
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


@pytest.mark.parametrize("a, b, expected_exception, expected_message", [(0, 5, ValueError, "Cannot take log of non-positive number!"), (-2, 5, ValueError, "Cannot take log of non-positive number!"), (5, 1, NameError, "Cannot take log with base 1!"), (5, 0, ZeroDivisionError, "Cannot take log with non-positive base!")],)
def test_log(expected_exception, expected_message, a, b):
    with pytest.raises(expected_exception) as exc:
        calculator.log(a, b)
    assert str(exc.value) == expected_message




@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, 1, (-1.0, -1.0)),
        (1, -3, 2, (2.0, 1.0)),
        (2, 5, -3, (0.5, -3.0)),
        (1, -1000000, 1, (999999.999999, 1.00000761449337e-06)),
    ],
)
def test_correct_results(a, b, c, expected):
    assert solve_quadratic_formula(a, b, c) == expected

@pytest.mark.parametrize(
    "a, b, c, expected_exception",
    [
        ("a", 2, 1, TypeError),
        (1, [2], 1, TypeError),
        (1, 2, None, TypeError),
        (0, 2, 1, SyntaxError),
        (1, 5, 1, NameError),
        (1, 2, 5, ValueError),
    ],
)
def test_exceptions(a, b, c, expected_exception):
    with pytest.raises(expected_exception):
        solve_quadratic_formula(a, b, c)

if __name__ == "__main__":
    pytest.main()




