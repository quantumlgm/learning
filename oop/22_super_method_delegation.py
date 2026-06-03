# Design a base class `Employee` and a subclass `TechLead` to 
# demonstrate class extension, method overriding, and delegation 
# using the `super()` function.

# Requirements:
# 1. Base Class `Employee`:
#    - `__init__` accepts and stores `name` (str) and `base_salary` (int/float).
#    - Method `get_total_salary()` returns the `base_salary`.

# 2. Subclass `TechLead`:
#    - Inherits from `Employee`.
#    - Extends `__init__` to also accept a `bonus` (int/float). 
#      It MUST use `super()` to delegate the initialization 
#      of `name` and `base_salary` to the parent class.
#    - Overrides `get_total_salary()` by using `super()` to fetch the 
#      parent's total salary and then adds the `bonus` to it.
#    - Extends the class by adding a unique method `conduct_meeting()` 
#      that returns a string specific to a tech lead's duties.


class Employee:
    def __init__(self, name: str, base_salary: int | float) -> None:
        self.name = name
        self.base_salary = base_salary

    def get_total_salary(self):
        return self.base_salary
    
class TechLead(Employee):
    def __init__(self, name: str, base_salary: int | float, bonus: int) -> None:
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def get_total_salary(self) -> int | float:            
        return self.bonus + super().get_total_salary()
    
    def conduct_meeting(self) -> str:
        return f'Teamlead {self.name} is holding a technical conference call'
    
if __name__ == "__main__":
    employe = Employee('Quantum', 100000)
    print(employe.__dict__) # {'name': 'Quantum', 'base_salary': 100000}
    print(employe.get_total_salary()) # 100000
    lead = TechLead('Ruslan', 150000, 10000)
    print(lead.__dict__) # {'name': 'Ruslan', 'base_salary': 150000, 'bonus': 10000}
    print(lead.get_total_salary()) # 160000
    print(lead.conduct_meeting()) # Teamlead Ruslan is holding a technical conference call