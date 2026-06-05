# Design an `AuthSystem` class to demonstrate exception propagation 
# through a call stack, showing how an exception raised in 
# a deeply nested method travels up to be caught at the top level.

# Requirements:
# 1. Class `AuthSystem`:
#    - Implement a private method `_db_fetch_user(username: str) -> dict`. 
#      If username is "admin", return {"username": "admin", "role": "root"}. 
#      For any other username, intentionally trigger a `KeyError` (e.g., accessing a 
#      missing key in an empty dict `{}[username]`) without wrapping it in try-except.
#    - Implement a private method `_verify_access(username: str) -> str`. 
#       It must call `_db_fetch_user(username)`. If the role is "root", return "Access Granted". 
#       Do NOT catch exceptions here.
#    - Implement a public method `authenticate(username: str) -> str`. 
#       Wrap the call to `_verify_access(username)` in a try-except block. 
#       Catch `KeyError` and return "Auth Error: User not found". If successful, 
#       return the granted access message.

