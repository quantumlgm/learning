"""
Lesson 07: Liskov Substitution Principle (LSP)

Short Description:
A notification delivery module demonstrating the SOLID Liskov Substitution Principle 
by ensuring that subclasses remain fully compatible with base class behavior.

Detailed Description:
This module adheres to LSP through strict behavioral design:
- 'EmailNotification' expands the input pre-conditions by accepting 'str | Sequence[str]' 
  instead of just 'str', keeping the type system safe and flexible.
- 'SMSNotification' adds an optional 'phone' parameter with a default value, ensuring 
  it doesn't break the base class signature for existing clients.
- All subclasses preserve post-conditions and invariants by consistently returning a 
  'bool' and avoiding unexpected runtime exceptions.
"""

import random
from collections.abc import Sequence


class Notification:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def send(self, message: str) -> bool:
        result = random.choice([True, False])
        if result:
            self.messages.append(message)
        return result


class EmailNotification(Notification):
    def send(self, message: str | Sequence[str]) -> bool:
        result = random.choice([True, False])
        if result:
            if isinstance(message, str):
                self.messages.append(message)
            else:
                self.messages.extend(message)
        return result


class SMSNotification(Notification):
    def send(self, message: str, phone: int = 900) -> bool:
        result = random.choice([True, False])
        if result:
            self.messages.append(f"[{phone}]: {message}")
        return result


if __name__ == "__main__":

    def delivery(notifier: Notification) -> None:
        success = notifier.send("Hello!")
        print(f"Status of answer: {success}, log: {notifier.messages}")

    base_notif = Notification()
    email_notif = EmailNotification()
    sms_notif = SMSNotification()

    delivery(base_notif)  # Status of answer: False, log: []
    delivery(email_notif)  # Status of answer: True, log: ['Hello!']
    delivery(sms_notif)  # Status of answer: False, log: []
