from pathlib import Path

nama = input("Siapa namamu? ")

lokasi = Path("Python_Raka_095/Exercise/exercise10_4.txt")
lokasi.write_text(nama)
print(f"Nama {nama} sudah disimpan di {lokasi}.")