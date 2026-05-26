# Design a class named `WindowSettings` that implements the Monostate (Borg)
# pattern, ensuring that all instances share the same state (attributes).

# Requirements:
# 1. Shared State:
#    - Define a private class-level dictionary to store shared attributes.
#    - Initialize it with default values: `theme` set to "dark" and `font_size` set to 14.

# 2. Initialization:
#    - The `__init__` method must accept two parameters: `width` (int) and `height` (int).
#    - Ensure that every new instance points to the class-level shared dictionary
#      instead of creating its own local `__dict__`.
#    - Update the shared dictionary with the provided `width` and `height`
#      values during instantiation.


class WindowSettings:
    __attr = {
        "theme": "dark",
        "font-size": 14,
    }

    def __init__(self, width, height):
        self.__dict__ = self.__attr
        self.__attr["width"] = width
        self.__attr["height"] = height


if __name__ == "__main__":
    Window_1 =  WindowSettings(100, 200)
    print(Window_1.__dict__) # {'theme': 'dark', 'font-size': 14, 'width': 100, 'height': 200}
    Window_2 =  WindowSettings(200, 300)
    print(Window_2.__dict__) # {'theme': 'dark', 'font-size': 14, 'width': 200, 'height': 300}    

