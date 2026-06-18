from typing import Protocol
from abc import ABC


class ContractProtocol(Protocol):
    def close(self) -> None: ...


class ContractABC(ABC):
    def close(self) -> None:
        print("The app is closing from ABC...")


class CloseFromABC(ABC):
    def close(self) -> None:
        print("The app is closing from CloseFromABC...")


class CloseFromProtocol:
    def close(self) -> None:
        print("The app is closing...")


def close_protocol(interface: ContractProtocol):
    interface.close()


def close_abc(interface: CloseFromABC):
    interface.close()


if __name__ == "__main__":
    close_protocol(CloseFromProtocol())  # The app is closing...
    """
    close_abc(CloseFromProtocol())

    Even though both classes possess the "close" method, 
    Pyright flags this as an error. This happens because ABCs 
    enforce nominal typing, meaning explicit inheritance is strictly required.
    """

    close_abc(CloseFromABC())  # The app is closing from CloseFromABC...
