"""
Design a class named `User` that overrides custom equality (`__eq__`)
and hashing (`__hash__`) behaviors to ensure that uniqueness is
strictly determined by the `username` field.

Requirements:
1. Initialization:
   - Accepts `username` (str) and `email` (str).

2. Magic Methods:
   - Implement `__eq__`: Two `User` instances are equal if and only
     if their `username` values are identical. Return NotImplemented for other types.
   - Implement `__hash__`: Calculate the hash value based exclusively
     on the `username` attribute, allowing `User` objects to be safely stored in sets and
     used as dictionary keys.
   - Implement `__repr__`: Return a developer-friendly representation
     like: User(username='name').
"""


class User:
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def __eq__(self, value):
        if isinstance(value, User) and self.username == value.username:
            return True
        return NotImplemented

    def __hash__(self):
        return hash(self.username)

    def __repr__(self):
        return f"User(username='{self.username}'"


if __name__ == "__main__":
    user1 = User("quantum", "quantum@gmail.com")
    user2 = User("quantum", "quantum@gmail.com")
    user3 = User("ruslan", "ruslan@gmail.com")

    print(user1 == user2)  # True
    print(user1 == user3)  # False
    print(hash(user1) == hash(user2))  # True
    users = {user1, user2, user3}
    print(users)  # {User(username='ruslan', User(username='quantum'}
