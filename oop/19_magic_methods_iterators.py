# Design a class named `Countdown` that implements custom
# iteration behavior to simulate a countdown timer.

# Requirements:
# 1. Properties to store: starting integer value.
# 2. Implement custom iteration capability allowing the instance
#    to be used directly in a `for` loop.
# 3. Each iteration step must yield the current countdown value and
#    decrement the counter.
# 4. The countdown must include `0`. After yielding `0`, the next iteration
#    must raise the appropriate built-in exception to gracefully terminate the loop.


from __future__ import annotations


class Countdown:
    def __init__(self, start: int = 1, count: int = 1) -> None:
        if not isinstance(start, int) or not isinstance(count, int):
            raise ValueError("Values must be strictly numeric")

        self.start = start
        self.count = count

    def __iter__(self) -> Countdown:
        return self

    def __next__(self) -> int:
        if self.start < 0:
            raise StopIteration

        value = self.start
        self.start -= self.count
        return value


if __name__ == "__main__":
    counter = Countdown(10, 1)
    for i in counter:
        print(i)  # 10 9 8 7 6 5 4 3 2 1 0
