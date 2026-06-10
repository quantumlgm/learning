from dataclasses import dataclass, InitVar, field
from pprint import pprint


@dataclass
class EmployeModule:
    first_name: str
    last_name: str
    salary: float | int
    token: str = field(repr=False, compare=False)
    password: InitVar[str]
    skills: str = field(default_factory=list, compare=False)
    annual_income: float = field(init=False)


    def __post_init__(self, password: str):
        self.password_hash = password[::-1]
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.annual_income = self.salary * 12


if __name__ == "__main__":
    EmployeRuslan = EmployeModule(
        'ruslan', 'QuantUm', 2000, '#token007', 'temp_password', ['Python', 'C++', 'Go']
    )
    pprint(EmployeRuslan) # ->
    """
    EmployeModule(
        first_name='Ruslan',
        last_name='Quantum',
        salary=2000,
        skills=['Python', 'C++', 'Go'],
        annual_income=24000)
    """
    pprint(EmployeRuslan.__dict__) # ->
    """
    {'annual_income': 24000,
     'first_name': 'Ruslan',
     'last_name': 'Quantum',
     'password_hash': 'drowssap_pmet',
     'salary': 2000,
     'skills': ['Python', 'C++', 'Go'],
     'token': '#token007'}
    """
    
    EmployeRuslanOld = EmployeModule(
        'Ruslan', 'Quantum', 2000, "THERE ISN'T A TOKEN", 'NO PASSWORD', ['Python', 'C++', 'Go']
    )
    print(EmployeRuslan == EmployeRuslanOld) # True

    Cleaner = EmployeModule(
        'Glenn ', 'Matthews', 4000, 'wn3241njinf', '12489jfnfr'
    )
    pprint(Cleaner)
    """
    EmployeModule(first_name='Glenn ',
        last_name='Matthews',
        salary=4000,
        skills=[],
        annual_income=48000)
    """

