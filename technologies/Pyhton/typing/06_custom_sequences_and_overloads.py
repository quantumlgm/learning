"""
Lesson 06: Custom Sequences and Overloads

Short Description:
A custom request history tracker implementing the collections.abc.Sequence 
interface, backed by an internal dictionary with strict type overloads for slicing.

Detailed Description:
This module demonstrates how to build custom Python collections at a Senior level:
- 'RequestHistory' inherits from 'Sequence[RequestLog]', fulfilling the structural 
  contract by implementing the required '__len__' and '__getitem__' methods.
- Uses 'typing.overload' to explicitly map the dual behavior of '__getitem__': 
  passing an 'int' guarantees a single 'RequestLog' output, while passing a 'slice' 
  guarantees a new 'Sequence[RequestLog]' (sub-history) container.
- Demonstrates 'Type Narrowing' via 'isinstance(key, slice)' to handle internal 
  routing safely and clear static analysis warnings in Pyright.
"""

from typing import TypeVar, overload
from collections.abc import Sequence
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class RequestLog:
    content: str
    url: str
    data: int


class RequestHistory(Sequence[RequestLog]):
    def __init__(self, data: list[RequestLog]):
        self._storage: dict[int, RequestLog] = {}
        for key, value in enumerate(data):
            self._storage[key] = value

    def __len__(self) -> int:
        return len(self._storage)

    @overload
    def __getitem__(self, key: int) -> RequestLog: ...

    @overload
    def __getitem__(self, key: slice) -> Sequence[RequestLog]: ...

    def __getitem__(self, key: int | slice) -> RequestLog | Sequence[RequestLog]:
        all_logs = list(self._storage.values())
        if isinstance(key, slice):
            sliced_logs = all_logs[key]
            return RequestHistory(sliced_logs)
        return all_logs[key]

    def __repr__(self) -> str:
        logs_list = list(self._storage.values())
        return f"RequestHistory({logs_list})"


if __name__ == "__main__":
    error_log = RequestLog("error", "https://www.a", 10)
    success_log = RequestLog("success", "https://www.b", 20)
    load_log = RequestLog("load", "https://www.c", 30)

    history = RequestHistory([error_log, success_log, load_log])
    print(len(history))  # 3
    print(history[1])  # RequestLog(content='success', url='https://www.b', data=20)
    print(
        history[0:2]
    )  # RequestHistory([RequestLog(content='error', url='https://www.a', data=10), RequestLog(content='success', url='https://www.b', data=20)])
