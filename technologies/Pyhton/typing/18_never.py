"""
Lesson 18: NoReturn vs. Never

Short Description:
Differentiating between terminal function control flow and type exhaustiveness checking.

Detailed Description:
This module demonstrates the semantic separation between NoReturn and Never:
- Uses 'NoReturn' for 'force_shutdown' to signal that the function never yields control back.
- Uses 'Never' in 'any_color' to enforce strict compile-time exhaustiveness checking.
- Proves that if the 'Color' Literal expands without a corresponding handling branch, 
  Pyright will raise a type mismatch error before the code even runs.
"""

from typing import NoReturn, Literal, Never


def force_shutdown() -> NoReturn:
    raise SystemExit("You know unique color! Pleace contact with us")

def any_color(arg: Never) -> Never:
    raise ValueError(f"Argument: {arg} does not match any of the accepted types")

    
Color = Literal["red", "green", "chartreuse"]


def process_color(color: Color):
    if color == "red":
        print("Red means speed!")
    elif color == "green":
        print("Green means life!")
    elif color == "chartreuse":
        force_shutdown()
    else:
        any_color(color) 
        """
        The IDE tells us that this condition is never expected
        """

if __name__ == "__main__":
    process_color("red") # Red means speed!
    process_color("green") # Green means life!                                                                
    process_color("chartreuse") # You know unique color! Pleace contact with us

    """
    But if we switch the order of the function calls 
    with unexpected arguments, this is exactly what will be printed
    """
    process_color("anything") # Argument: anything does not match any of the accepted types

    




