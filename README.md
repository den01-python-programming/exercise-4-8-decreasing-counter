# Exercise 4.8 Decreasing counter

This exercise consists of multiple parts.

The exercise template comes with a partially executed class `decreasing_counter`:

```python
class DecreasingCounter:

    def __init__(self,initial_value):
        self.value = initial_value

    def print_value(self):
        print("value: " + str(self.value))

    def decrement(self):
        # write the method implementation here
        # the aim is to decrement the value of the counter by one

    # and the other methods go here
```

The following is an example of how the main program uses the decreasing counter:

```python
from decreasing_counter import DecreasingCounter

def main():
    counter = DecreasingCounter(10)

    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()
```

The program above should have the following print output.

```plaintext

value: 10
value: 9
value: 8

```

## Implementation of the decrement() method

Implement the `decrement()` method in the class body in such a way that it decrements the `value` variable of the object it's being called on by one. Once you're done with the `decrement()` method, the main program of the previous example should work to produce the example output.

## The counter's value cannot be negative

Implement the `decrement()` in such a way that the counter's value never becomes negative. This means that if the value of the counter is 0, it cannot be decremented. A conditional statement is useful here.

```python
def main():
    counter = DecreasingCounter(2)

    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()

    counter.decrement()
    counter.print_value()
```
Prints:

```plaintext
value: 2
value: 1
value: 0
value: 0
```

## Resetting the counter value

Create the method `def reset()` for the counter that resets the value of the counter to 0. For example:

```python
def main():
    counter = DecreasingCounter(100)

    counter.print_value()

    counter.reset()
    counter.print_value()

    counter.decrement()
    counter.print_value()
```

Prints:

```plaintext
value: 100
value: 0
value: 0
```
