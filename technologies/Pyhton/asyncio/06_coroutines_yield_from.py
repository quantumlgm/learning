"""
Lesson 6: Coroutines, Bidirectional Data Pipelines, and Generator Delegation via 'yield from'.

This program explores the mechanics of Python coroutines using advanced generator methods, 
focusing on pushing data into suspended frames and orchestrating subgenerators without manual loop plumbing.

Key Features:
- Bidirectional Execution Flow: Demonstrates the dual nature of 'yield' acting as an expression 
  that receives external data injected via the '.send()' protocol.
- Subgenerator Delegation: Utilizes 'yield from' to establish a direct, transparent pipeline 
  between the caller code and the inner 'packer' coroutine, bypassing manual iteration loops.
- Automatic Exception and Signal Routing: Leverages 'yield from' to natively handle internal 
  throw mechanisms and catch 'StopIteration' boundaries across the generator chain.
- Seamless Value Return: Showcases how 'yield from' automatically captures the final 'return' 
  value of an exhausted subgenerator and assigns it to a local variable in the delegator.
"""

def packer():
    weight = 0
    while True:
        weight += yield
        if weight >= 10:
            return f"The box({weight}kg) was been sent to delivery service"
        print(f"The box with weight: {weight} recived")


def dispatcher():
    result = yield from packer()
    print(f"Result of packer work: {result}")


if __name__ == "__main__":
    d = dispatcher()
    next(d)

    d.send(5)  # The box with weight: 5 recived
    d.send(2)  # The box with weight: 7 recived
    d.send(15)  # Result of packer work: The box(22kg) was been sent to delivery service
                #  StopIteration
