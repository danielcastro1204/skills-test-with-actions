import pytest
from src.calculations import get_nth_fibonacci

def test_fibonacci_zero():
    """Cover base case for n = 0 (if implemented)."""
    try:
        result = get_nth_fibonacci(0)
        assert result == 0 or result == 1
    except ValueError:
        assert True

def test_fibonacci_negative():
    """Cover error handling for negative n."""
    with pytest.raises((ValueError, TypeError)):
        get_nth_fibonacci(-1)