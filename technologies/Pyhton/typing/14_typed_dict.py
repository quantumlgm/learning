"""
Lesson 14: TypedDict and Discriminated Unions

Short Description:
An implementation of structured dictionaries with fixed keys using TypedDict
and type narrowing via literal markers.

Detailed Description:
This module demonstrates how to type JSON-like dictionary structures safely:
- 'SuccessAnswer' and 'ErrorAnswer' declare strict key-value pairs.
- Uses 'NotRequired' to handle optional configuration keys without breaking validation.
- Leverages 'Literal' fields ("ok" / "fail") as discriminants to allow Pyright
  to perform reliable type narrowing within conditional blocks.
"""

from typing import TypedDict, Literal, NotRequired


class SuccessAnswer(TypedDict):
    status: Literal["ok"]
    data: list[str]
    token: NotRequired[str]


class ErrorAnswer(TypedDict):
    status: Literal["fail"]
    code: int


type Answer = SuccessAnswer | ErrorAnswer


def process_api_response(answer: Answer):
    if answer["status"] == "ok":
        return answer["data"]
    else:
        return f"Error: {answer['status']}, status: {answer['code']}"


if __name__ == "__main__":
    succes_answer: SuccessAnswer = {
        "status": "ok",
        "data": ["Quantum", "Ruslan", "Github"],
    }
    print(process_api_response(succes_answer))  # ['Quantum', 'Ruslan', 'Github']

    error_answer: ErrorAnswer = {"status": "fail", "code": 404}
    print(process_api_response(error_answer))  # Error: fail, status: 404
