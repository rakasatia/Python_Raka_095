import pytest

from exercise11_3a import Employee


@pytest.fixture
def employee():
    """Menyediakan instance pegawai untuk setiap fungsi test."""
    return Employee("Budi", "Santoso", 65000)


def test_give_default_raise(employee):
    """Menguji kenaikan gaji bawaan menggunakan fixture."""
    employee.give_raise()
    assert employee.annual_salary == 70000


def test_give_custom_raise(employee):
    """Menguji kenaikan gaji khusus menggunakan fixture."""
    employee.give_raise(10000)
    assert employee.annual_salary == 75000
