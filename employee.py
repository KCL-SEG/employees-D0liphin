import typing


class SalaryContract:
    def __init__(self, salary: float):
        self.salary = salary

    def total_pay(self) -> float:
        return self.salary

    def __str__(self) -> str:
        return f"monthly salary of {int(self.salary)}"


class HourlyContract:
    def __init__(self, hourly_rate: float, hours: float):
        self.hourly_rate = hourly_rate
        self.hours = hours

    def total_pay(self) -> float:
        return self.hourly_rate * self.hours

    def __str__(self) -> str:
        return f"contract of {int(self.hours)} hours at {int(self.hourly_rate)}/hour"


Contract = typing.Union[SalaryContract, HourlyContract]


class BonusCommission:
    def __init__(self, value: float):
        self.value = value

    def get_value(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"bonus commission of {int(self.value)}"


class ContractCommission:
    def __init__(self, value: float, count: int):
        self.value = value
        self.count = count

    def get_value(self) -> float:
        return self.value * self.count

    def __str__(self) -> str:
        return f"commission for {self.count} contract(s) at {self.value}/contract"


Commission = typing.Union[BonusCommission, ContractCommission]


class Employee:
    def __init__(self, name: str, contract: Contract, commission: typing.Optional[Commission]):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self) -> int:
        """
        return this employee's pay as an integer
        """
        return int(self.contract.total_pay() + (self.commission.get_value() if self.commission != None else 0))

    def __str__(self):
        return f"{self.name} works on a {self.contract}" + \
            (f" and receives a {self.commission}. " if self.commission != None else ". ") +\
            f"Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', SalaryContract(4000), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25, 100), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', SalaryContract(3000), ContractCommission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', SalaryContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))

