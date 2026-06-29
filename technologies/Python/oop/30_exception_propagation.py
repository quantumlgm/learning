"""
Design an `AuthSystem` class to demonstrate exception propagation
through a call stack, showing how an exception raised in
a deeply nested method travels up to be caught at the top level.

Requirements:
1. Class `AuthSystem`:
   - Implement a private method `_db_fetch_user(username: str) -> dict`.
     If username is "admin", return {"username": "admin", "role": "root"}.
     For any other username, intentionally trigger a `KeyError` (e.g., accessing a
     missing key in an empty dict `{}[username]`) without wrapping it in try-except.
   - Implement a private method `_verify_access(username: str) -> str`.
      It must call `_db_fetch_user(username)`. If the role is "root", return "Access Granted".
      Do NOT catch exceptions here.
   - Implement a public method `authenticate(username: str) -> str`.
      Wrap the call to `_verify_access(username)` in a try-except block.
      Catch `KeyError` and return "Auth Error: User not found". If successful,
      return the granted access message.
"""


class AuthSystem:
    def _db_fetch_user(self, username: str) -> dict:
        if username == "admin":
            return {"username": "admin", "role": "root"}
        raise KeyError("The user isn't in the base")

    def _verify_access(self, username: str) -> str:
        user_data = self._db_fetch_user(username)
        if user_data["role"]:
            return "Access Granted"

    def authenticate(self, username: str) -> str:
        try:
            result = self._verify_access(username)
            return result
        except KeyError:
            return "Auth Error: User not found"


if __name__ == "__main__":
    user = AuthSystem()
    try:
        user._db_fetch_user("ruslan")
    except:
        print(
            "KeyError: 'The user isn't in the base'"
        )  # KeyError: 'The user isn't in the base'

    user._db_fetch_user("admin")

    print(user._verify_access("admin"))  # Access Granted

    print(user.authenticate("ruslan"))  # Auth Error: User not found
    print(user.authenticate("admin"))  # Access Granted

    