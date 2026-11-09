import json
from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_11.json")
angka = json.loads(lokasi.read_text())
print(f"Aku tahu angka favoritmu! Yaitu {angka}.")