# Design a base class `NotificationSender` and two subclasses 
# `TelegramSender` and `EmailSender` to demonstrate class inheritance 
# and method/property overriding.

# Requirements:
# 1. Base Class `NotificationSender`:
#    - `__init__` accepts and stores `sender_name` (str).
#    - Method `send(user, message)` returns a formatted string 
#      containing sender_name, user, and message.

# 2. Subclass `TelegramSender`:
#    - Inherits from `NotificationSender`.
#    - Overrides/adds property `platform_name` set to "Telegram".
#    - Overrides `send` method to include an emoji and platform_name 
#      in its return string.

# 3. Subclass `EmailSender`:
#    - Inherits from `NotificationSender`.
#    - Overrides/adds property `platform_name` set to "Email".
#    - Overrides `send` method to include a different emoji and 
#      platform_name in its return string.


class NotificationSender:
    def __init__(self, sender_name: str):
        if not isinstance(sender_name, str):
            raise ValueError("Values must be a string")
        self._sender_name = sender_name

    def send(self, user: str, message: str) -> str:
        return f'[{self._sender_name}] Notification for {user}: {message}'
    

class TelegramSender(NotificationSender):
    _platform_name = 'Telegram'

    def send(self, user: str, message: str) -> str:
        return f'{self._platform_name} | {self._sender_name} sending for {user}: {message}'
    
class EmailSender(NotificationSender):
    _platform_name = 'Email'

    def send(self, user: str, message: str) -> str:
        return f'{self._platform_name} | Letter from {self._sender_name} for {user} -> {message}'
    

if __name__ == '__main__':
    Notification = NotificationSender('RuslanN')
    print(Notification.__dict__) # {'_sender_name': 'RuslanN'}

    Telegram = TelegramSender('RuslanT')
    print(Telegram.__dict__) # {'_sender_name': 'RuslanT'}

    Email = EmailSender('RuslanE')
    print(Email.__dict__) # {'_sender_name': 'RuslanE'}
    
    print(Notification.send('Linus Torvalds', 'This notification for you!')) # [RuslanN] Notification for Linus Torvalds: This notification for you!
    print(Telegram.send('Linus Torvalds', 'Hello dude!')) # Telegram | RuslanT sending for Linus Torvalds: Hello dude!
    print(Email.send('LinusTorvalds@gmail.com', "I'm looking forward to hearing from you!")) # Email | Letter from RuslanE for LinusTorvalds@gmail.com -> I'm looking forward to hearing from you!