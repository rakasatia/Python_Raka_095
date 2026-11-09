from exercise11_3a import Employee


def test_give_default_raise():
    """Menguji kenaikan gaji bawaan sebesar 5.000."""
    employee = Employee("Budi", "Santoso", 65000)
    employee.give_raise()
    assert employee.annual_salary == 70000


def test_give_custom_raise():
    """Menguji kenaikan gaji dengan nilai khusus."""
    employee = Employee("Budi", "Santoso", 65000)
    employee.give_raise(10000)
    assert employee.annual_salary == 75000
