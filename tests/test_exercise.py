import pytest
from src.decreasing_counter import DecreasingCounter

def test_exercise(capsys):
    counter = DecreasingCounter(10)

    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    out, err = capsys.readouterr()
    assert out == "value: 10\nvalue: 9\nvalue: 8\n"

    counter = DecreasingCounter(2)

    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    out, err = capsys.readouterr()
    assert out == "value: 2\nvalue: 1\nvalue: 0\nvalue: 0\n"
