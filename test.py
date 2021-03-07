import pytest

from main import fizzBuzz

def test_fizz():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(6) == "Fizz"
    assert fizzBuzz(10) == "Buzz"

