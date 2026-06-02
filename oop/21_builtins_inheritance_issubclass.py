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


from typing import Any


class LoggingList(list):
    def append(self, item: Any) -> None:
        print(f'Item was added: {item}')
        list.append(self, item)


class StringLoggingList(LoggingList):
    def append(self, item: str) -> None:
        if not isinstance(item, str):
            raise ValueError("Value must be string")
        LoggingList.append(self, item)
        
    
if __name__ == '__main__':
    logging_list = LoggingList()
    logging_list.append('Quantumlgm') # Item was added: Quantumlgm
    
    string_logging_list = StringLoggingList()
    string_logging_list.append('Quantumlgm String') # Item was added: Quantumlgm String
#   string_logging_list.append(100) -> ValueError: Value must be string