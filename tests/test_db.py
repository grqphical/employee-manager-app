from app import interfaces

def test_get_employees():
    assert interfaces.get_employees() == [('Joe', 'Mama', 60000, 'Joe.Mama@company.com'), ('John', 'Doe', 100000, 'John.Doe@company.com'), ('Jane', 'Doe', 80000, 'Jane.Doe@company.com'), ('Mike', 'Rochburns', 75000, 'Mike.Rochburns@company.com')]

def test_get_employee():
    assert interfaces.get_employees_by_last("Doe") == [('John', 'Doe', 100000, 'John.Doe@company.com'), ('Jane', 'Doe', 80000, 'Jane.Doe@company.com')]