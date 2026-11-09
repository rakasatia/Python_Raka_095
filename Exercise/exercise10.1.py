from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_1.txt")

print("--- Cara 1: membaca seluruh file ---")
isi = lokasi.read_text(encoding="utf-8")
print(isi)

print("--- Cara 2: menyimpan baris dalam list lalu mengulanginya ---")
baris_baris = isi.splitlines()
for baris in baris_baris:
    print(baris)
