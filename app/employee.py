class Employee:
    """Class used to represent employee data"""
    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    @property
    def email(self):
        return f"{self.firstName}.{self.lastName}@company.com"