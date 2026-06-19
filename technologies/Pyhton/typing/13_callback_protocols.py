"""
Lesson 13: Callback Protocols and Advanced Function Overloading

Short Description:
A deep dive into replacing standard 'Callable' types with structural 
Callback Protocols featuring precise parameter naming and static constraints.

Detailed Description:
This module demonstrates how to enforce strict type contracts on functions higher in the stack:
- Employs '__call__' inside a Protocol to provide descriptive signatures.
- Utilizes multiple '@overload' definitions within the protocol to link input types 
  directly to expected outputs (e.g., mapping 'str' to 'int' and 'int' to 'list[str]').
- Highlights how strict static analysis (Pyright) validates implementation compliance 
  and type narrowing contexts.
"""

from typing import Protocol, overload

class CallbackInterface(Protocol):
    @overload
    def __call__(self, data: str) -> int: ...
    
    @overload
    def __call__(self, data: int) -> list[str]: ...    


def process(data: str | int, handler: CallbackInterface) -> None:
    if isinstance(data, str):
        result_int: int = handler(data)        
        print(result_int)
    else:
        result_list: list[str] = handler(data)
        print(result_list)
    

@overload
def smart_worker(data: str) -> int: ...


@overload
def smart_worker(data: int) -> list[str]: ...

def smart_worker(data: str | int):
    if isinstance(data, str):
        return len(data)    
    return [str(data)]

if __name__ == "__main__":
    process("Hello", smart_worker)  # 5
    process(42, smart_worker)  # ['42']