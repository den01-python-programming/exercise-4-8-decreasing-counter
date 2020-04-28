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
    assert out == "10\n9\n8\n"

    counter = DecreasingCounter(2)

    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    out, err = capsys.readouterr()
    assert out == "2\n1\n0\n0"
