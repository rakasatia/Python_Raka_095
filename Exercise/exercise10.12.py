import json
from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_12.json")

try:
    isi = lokasi.read_text(encoding="utf-8")
except FileNotFoundError:
    angka_favorit = input("Berapa angka favoritmu? ")
    isi = json.dumps(angka_favorit)
    lokasi.write_text(isi, encoding="utf-8")
    print("Terima kasih! Aku akan mengingat angka favoritmu.")
else:
    angka_favorit = json.loads(isi)
    print(f"Aku tahu angka favoritmu! Yaitu {angka_favorit}.")
