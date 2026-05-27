# Design a class named `CreatePerson` to store and validate employee records using properties.
# This task serves as a milestone check for encapsulation and descriptor properties.

# Requirements:
# 1. Initialization:
#    - Accepts `fio` (str) and `age` (int).
#    - Must initialize attributes by routing values through their
#      respective property setters.

# 2. FIO Property:
#    - Getter: Returns the protected list of names joined back into a single string,
#      with each word capitalized (e.g., "John Doe Smith").
#    - Setter: Accepts a raw string. Validates that the input is a string and
#      contains exactly 3 words. If invalid, raises a ValueError. If valid,
#      strips extra spaces, splits it into a list, and stores it in `_fio`.

# 3. Age Property:
#    - Getter: Returns the integer age.
#    - Setter: Accepts an integer. Validates that the age is between 18 and 65 (inclusive).
#      Raises a ValueError if validation fails. Otherwise, stores it in `_age`.


class CreatePerson:
    def __init__(self, fio: str, age: int) -> None:
        self.fio = fio
        self.age = age

    @property
    def fio(self) -> str:
        return " ".join(self._fio)

    @fio.setter
    def fio(self, new_fio: str):
        if len(new_fio.split()) < 3:
            raise ValueError("Incorrect format for the full name")
        self._fio = [word.capitalize() for word in new_fio.split()]

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int):
        if not isinstance(new_age, int):
            raise ValueError("Incorrect format for the age")
        if not (new_age >= 18 and new_age <= 65):
            raise ValueError("Age is outside the permitted range ")
        self._age = new_age


if __name__ == "__main__":
    Person = CreatePerson("ruslan Quantum Lgm", 19)
    print(Person.__dict__)  # {'_fio': ['Ruslan', 'Quantum', 'Lgm'], 'age': 18}
    print(Person.fio)  # Ruslan Quantum Lgm
    Person.fio = "Ruslan quantum Github"
    print(Person.__dict__)  # {'_fio': ['Ruslan', 'Quantum', 'Github'], 'age': 18}
    print(Person.age)
    # Person.age = 66 # ValueError: Age is outside the permitted range
    Person.age = 20
    print(Person.__dict__)  # {'_fio': ['Ruslan', 'Quantum', 'Github'], '_age': 20}
