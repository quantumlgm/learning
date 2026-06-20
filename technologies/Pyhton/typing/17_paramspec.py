"""
Lesson 17: ParamSpec and Concatenate

Short Description:
Preserving and modifying function signatures within decorators using ParamSpec and Concatenate.

Detailed Description:
This module demonstrates advanced typing for decorators and closures:
- Uses 'ParamSpec' (P) to capture full argument signatures, preventing type erasure.
- Leverages 'P.args' and 'P.kwargs' to pass parameters safely through wrappers.
- Employs 'Concatenate' to explicitly model signature mutation, removing the first 
  'Database' positional argument from the decorated function's external interface.
"""

from typing import ParamSpec, TypeVar, Concatenate
from collections.abc import Callable

T = TypeVar("T")
P = ParamSpec("P")


class Database:
    pass

def simple_logger(func: Callable[P, T]):
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        print("The function starts")
        return func(*args, **kwargs)
    return wrapper

def inject_database(func: Callable[Concatenate[Database, P], T]):
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        db_obj = Database()
        return func(db_obj, *args, **kwargs)
    return wrapper

@simple_logger
def send_message(username: str, text: str) -> tuple[str, str]:
    return username, text

@inject_database
def get_user_data(db: Database, user_id: int, token: str) -> tuple[Database, int, str]:
    return db, user_id, token

if __name__ == "__main__":
    send_message('Hello', "world!") # The function starts
    get_user_data(user_id=1, token="@token111")