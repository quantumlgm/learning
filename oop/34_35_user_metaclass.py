"""
Task 33: Metaclasses.

This program implements a custom metaclass 'ClassChecker' that enforces
strict coding standards for API-related classes at the time of their creation.

Key Features:
- Class Validation: Automatically enforces that all classes using this
  metaclass must begin with the 'API' prefix, raising a NameError if not.
- Automatic Refactoring: Dynamically converts all method names from
  CamelCase to snake_case during class construction.
- Compliance Tracking: Injects a hidden '_is_api_compliant' attribute
  into every validated class.
- Metaprogramming: Utilizes the __new__ method of the metaclass to manipulate
  the class namespace before the class object is fully instantiated.
"""


class ClassChecker(type):
    def __new__(cls, name: str, bases: tuple, namespace: dict):
        if not name.startswith("API"):
            raise NameError(f"The class '{name}' must start with 'API' prefix")

        new_namespace = {}
        for key, value in namespace.items():
            if key.startswith("__"):
                new_namespace[key] = value
                continue

            new_name = ""
            for i, char in enumerate(key):
                if char.isupper() and i > 0:
                    new_name += "_" + char.lower()
                else:
                    new_name += char.lower()

            new_namespace[new_name] = value

        new_namespace["_is_api_compliant"] = True

        return super().__new__(cls, name, bases, new_namespace)


class APILoginHandler(metaclass=ClassChecker):
    def LoginUser(self):
        pass

    def Log_Out(self):
        pass


login_handler = APILoginHandler()
print(
    APILoginHandler.__dict__
)  # 'log_out': <func..., '_is_api_compliant': True, 'loginuser': <func...
print(login_handler.login_user())


class BadUncheckedClass(
    metaclass=ClassChecker
):  # NameError: The class 'BadUncheckedClass' must start with 'API' prefix
    pass
