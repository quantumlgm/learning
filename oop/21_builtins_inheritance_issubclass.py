# Design two classes, `LoggingList` and `StringLoggingList`, by extending 
# Python's built-in `list` type, and validate their hierarchy.

# Requirements:
# 1. Subclass `LoggingList`:
#    - Inherits directly from the built-in `list` class.
#    - Overrides the standard element-appending method to print 
#      f"Add item: {item}" to the console right before appending the item.

# 2. Subclass `StringLoggingList`:
#    - Inherits from `LoggingList`.
#    - Overrides the same element-appending method to strictly allow only 
#      strings (raise TypeError otherwise).

# 3. Validation:
#    - In the execution block, check class hierarchies using `issubclass()`.