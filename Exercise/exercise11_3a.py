class Employee:
    """Menyimpan informasi pegawai dan mengubah gaji tahunannya."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Menambahkan kenaikan pada gaji tahunan pegawai."""
        self.annual_salary += raise_amount
