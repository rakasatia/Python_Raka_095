import json
from pathlib import Path

angka = input("Berapa angka favoritmu? ")
lokasi = Path("Python_Raka_095/Exercise/exercise10_11.json")
lokasi.write_text(json.dumps(angka))
print("Angka favoritmu sudah disimpan!")