class Member:
    """
    Basic class for members in the company, identified only with name and address
    """

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} - Name: {self.name} - Address: {str(self.address)}"
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name: {self.name}, address: {self.address})"

    def __lt__(self, other):
        """
        Way of comparing/sorting members in the company
        The sorting is based on comparing string type of the employee (Employee class)
        If they are from the same category, they will be compared based on their salary 

        Args:
            self (Employee): First Employee
            other (Employee): Second Employee

        Returns:
            Boolean: Whether the first employee must come first or not based on our standards
        """
        if self.__class__.__name__ != other.__class__.__name__:
            return self.__class__.__name__ < other.__class__.__name__

        return (self.name, self.address) < (other.name, other.address)

class Volunteer(Member):
    """
    Just a type of Members in the company with specific monthly salary
    """

    def __init__(self, name: str, address: str, salary: float) -> None:
        super().__init__(name, address)
        self.salary = salary
        
    def total_payment(self) -> float:
        return self.salary

class Employee(Member):
    """
    Anther type of members in the company that will be classified according the way of payment
    This type of members has specific day of payment
    """

    def __init__(self, name: str, address: str, payment_day: str) -> None:
        super().__init__(name, address)
        self.payment_day = payment_day

class HourlyBasedEmployee(Employee):
    """
    An Employee which has Hourly Based Salary
    """

    def __init__(self, name: str, address: str, payment_day: str, total_working_hours: float, hourly_wage: float) -> None:
        super().__init__(name, address, payment_day)
        self.total_working_hours = total_working_hours
        self.hourly_wage = hourly_wage
    
    def total_payment(self) -> float:
        return self.total_working_hours * self.hourly_wage

class SalariedBasedEmployee(Employee):
    """
    An Employee which has Monthly Based Salary
    """
    
    def __init__(self, name: str, address: str, payment_day: str, salary_per_month: float) -> None:
        super().__init__(name, address, payment_day)
        self.salary_per_month = salary_per_month
    
    def total_payment(self) -> float:
        return self.salary_per_month

class ComissionSalariedBasedEmploee(SalariedBasedEmployee):
    """
    Also an employee with Monthly based salary but also get some commisions on his total amount of sales
    """
    
    def __init__(self, name: str, address: str, payment_day: str, salary_per_month: float, sales: float, commision_rate: float) -> None:
        super().__init__(name, address, payment_day, salary_per_month)
        self.sales = sales
        self.commision_rate = commision_rate
    
    def total_payment(self) -> float:
        return super().total_payment() + (self.sales * self.commision_rate)

