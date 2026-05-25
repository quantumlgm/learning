"""
Design a class named `EnvironmentConfig` that acts as a dynamic and secure configuration manager for an application.

Requirements:
1. The ` __init__` method must accept two parameters:
   - `defaults` (dict): A dictionary containing initial configuration keys and values.
   - `readonly_keys` (tuple/list): A collection of attribute names that cannot be modified or deleted after initialization.

2. During initialization, the class must dynamically turn all keys from the `defaults` dictionary into object attributes using built-in Python functions.

3. Implement a method `update_config(self, new_settings: dict) -> None` that safely iterates through the dictionary and updates or adds attributes.

4. Security constraints:
   - If a user attempts to delete a protected attribute (from `readonly_keys`), the deletion must be intercepted and prevented.
   - If a user attempts to overwrite a protected attribute with a new value, the modification must be ignored, keeping the original value intact.
   - If a user requests a non-existent attribute, instead of raising an AttributeError, the system should gracefully return the string "NOT_FOUND".

5. Use standard Python built-in tools for attribute manipulation: `getattr()`, `setattr()`, `hasattr()`, `delattr()`.
Do not implement custom dunder methods like `__getattr__` or `__setattr__` yet, rely entirely on standard functions within your custom logic.
"""


class EnvironmentConfig:
    def __init__(self, defaults: dict, readonly_keys: tuple) -> None:
        for key, value in defaults.items():
            setattr(self, key, value)

        self._readonly_keys = readonly_keys

    def get_config(self, key: str) -> str:
        if hasattr(self, key):
            return getattr(self, key)
        return "NOT_FOUND"

    def update_config(self, new_settings: dict) -> None:
        for key, value in new_settings.items():
            if key in self._readonly_keys:
                continue
            setattr(self, key, value)

    def del_config(self, key: str) -> dict:
        if hasattr(self, key):
            if key not in self._readonly_keys:
                delattr(self, key)
                return {"status_code": 200, "description": "Succesfully delete"}
            else:
                return {"status_code": 403, "description": "Item in the private list"}
        return {"status_code": 404, "description": "Item not found"}


if __name__ == "__main__":
    Environment = EnvironmentConfig(
        {"item1": 1, "item2": 2}, ("item1",)
    )  # Succesfully create
    print(Environment.__dict__)

    print(Environment.get_config("item1"))  # 1
    print(Environment.__dict__)

    Environment.update_config({"item2": 30})  # Successfully update
    print(Environment.__dict__)

    Environment.update_config({"item1": 10})  # Item in the private list
    print(Environment.__dict__)

    print(Environment.del_config("item2"))  # Successfully delete
    print(Environment.__dict__)

    print(Environment.del_config("item1"))  # Item in the private list
    print(Environment.__dict__)
