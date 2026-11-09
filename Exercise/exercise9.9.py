class Mobil:
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        self.bacaan_odometer = 0

    def nama_lengkap(self):
        nama_panjang = f"{self.tahun} {self.merek} {self.model}"
        return nama_panjang.title()

    def baca_odometer(self):
        print(f"Mobil ini sudah menempuh {self.bacaan_odometer} mil.")

    def perbarui_odometer(self, mil):
        if mil >= self.bacaan_odometer:
            self.bacaan_odometer = mil
        else:
            print("Kamu tidak boleh memundurkan odometer!")

    def tambah_odometer(self, mil):
        self.bacaan_odometer += mil


class Baterai:
    def __init__(self, ukuran_baterai=40):
        self.ukuran_baterai = ukuran_baterai

    def deskripsikan_baterai(self):
        print(f"Mobil ini punya baterai {self.ukuran_baterai}-kWh.")

    def hitung_jarak_tempuh(self):
        if self.ukuran_baterai == 40:
            jarak = 150
        elif self.ukuran_baterai == 65:
            jarak = 225

        print(f"Mobil ini bisa menempuh sekitar {jarak} mil dengan satu kali pengisian penuh.")

    def upgrade_baterai(self):
        if self.ukuran_baterai != 65:
            self.ukuran_baterai = 65


class MobilListrik(Mobil):
    def __init__(self, merek, model, tahun):
        super().__init__(merek, model, tahun)
        self.baterai = Baterai()


mobil_saya = MobilListrik("nissan", "leaf", 2024)
print(mobil_saya.nama_lengkap())
mobil_saya.baterai.deskripsikan_baterai()

mobil_saya.baterai.hitung_jarak_tempuh()   # sebelum upgrade
mobil_saya.baterai.upgrade_baterai()
mobil_saya.baterai.hitung_jarak_tempuh()   # sesudah upgrade