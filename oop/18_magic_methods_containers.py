# Design a class named `StudentJournal` that allows managing a student's
# academic grades directly using container emulation magic methods (square bracket syntax).

# Requirements:
# 1. Properties to store: student's name, collection of subject grades.
# 2. Implement retrieval by subject name.
# 3. Implement assignment/update by subject name.
# 4. Implement deletion by subject name.


class StudentJournal:
    def __init__(self, name: str, marks: dict) -> None:
        self.name = name
        if not isinstance(marks, dict):
            raise TypeError("The data type is incorrect")
        self.marks = marks

    def __getitem__(self, key: str) -> int:
        if key not in self.marks:
            raise ValueError("The item is not in the list")
        return self.marks[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.marks[key] = value

    def __delitem__(self, key: str) -> None:
        if key not in self.marks:
            raise ValueError("The item is not in the list")
        del self.marks[key]


if __name__ == "__main__":
    Student = StudentJournal("Ruslan", {"Math": 5, "History": 4, "CS": 5})
    print(Student["Math"])  # 5
    print(Student.marks)  # {'Math': 5, 'History': 4, 'CS': 5}

    Student["Math"] = 4
    print(Student["Math"])  # 4
    print(Student.marks)  # {'Math': 4, 'History': 4, 'CS': 5}

    del Student["History"]
    print(Student["History"])  # ValueError: The item is not in the list
    print(Student.marks)  # {'Math': 4, 'CS': 5}
