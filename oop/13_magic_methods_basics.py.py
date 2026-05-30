# Design a class named `Track` that represents an 
# audio recording and implements built-in Python behaviors using magic methods.

# Requirements:
# 1. Initialization:
#    - Accepts `title` (str), `artist` (str), 
#      `duration` (int in seconds), and `db_level` (int, can be negative).

# 2. Magic Methods:
#    - Implement `__repr__`: Returns a developer-friendly string formatted 
#      exactly as: Track('Title', 'Artist', duration, db_level).
#    - Implement `__str__`: Returns a user-friendly string formatted as: Artist — Title (duration sec.).
#    - Implement `__len__`: Returns the track's duration as an integer.
#    - Implement `__abs__`: Returns the absolute value of the db_level (removing the negative sign).

