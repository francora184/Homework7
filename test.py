import pytest

from main import fizzBuzz
from main import leapYear

def test_fizz():
    assert fizzBuzz(3) == "Fizz"
    assert fizzBuzz(6) == "Fizz"
    assert fizzBuzz(10) == "Buzz"
    assert fizzBuzz(15) == "FizzBuzz"

def test_leapyear():
    assert leapYear(2000) == "Yes"
    assert leapYear(1800) == "No"
    assert leapYear(2400) == "Yes"
    assert leapYear(1900) == "No"

    

