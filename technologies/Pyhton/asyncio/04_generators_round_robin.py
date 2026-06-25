"""
Lesson 4: Generator-Based Concurrency and Manual Round-Robin Event Loop.

This program demonstrates cooperative multitasking entirely within Python's native runtime,
bypassing operating system network stacks by shifting the concurrency model to Generators.

Key Features:
- State Preservation (Frames): Explores how generator functions maintain local execution state, 
  variables, and instruction pointers in memory without destroying the frame object upon yielding.
- Voluntary Control Yielding: Implements cooperative concurrency where functions deliberately 
  pause via the 'yield' keyword, returning flow control back to the central dispatcher.
- Round-Robin Scheduler: Constructs a single-threaded deterministic event loop using a simple 
  FIFO queue ('tasks') to rotate and advance independent execution contexts sequentially.
- Lifecycle Exhaustion Signal: Handles implicit task termination via standard 'StopIteration' 
  exceptions, isolating running tasks from finished execution streams.
"""

import time

def countdown_feed(duration: int):
    for sec in range(duration, 0, -1):
        time.sleep(1)
        yield sec

def gym_news(news: list[str]):
    while True:
        for new in news:
            time.sleep(2)
            yield new

news = [
    "New towels are waiting for you tomorrow!",
    "Maintain water balance!",
    "Cheer up and keep going!"
]

count_g = countdown_feed(10)
new_g = gym_news(news)

tasks = [count_g, new_g]

if __name__ == "__main__":
    while True:
        task = tasks.pop(0)

        try:        
            i = next(task)
            print(i)            
            tasks.append(task)            
        except StopIteration:
            break

    """
    10
    New towels are waiting for you tomorrow!
    9
    Maintain water balance!
    8
    Cheer up and keep going!
    7
    New towels are waiting for you tomorrow!
    """