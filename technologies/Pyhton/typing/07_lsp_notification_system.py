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

    delivery(base_notif) # Status of answer: False, log: []
    delivery(email_notif) # Status of answer: True, log: ['Hello!']
    delivery(sms_notif) # Status of answer: False, log: []