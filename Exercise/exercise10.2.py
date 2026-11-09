from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_1.txt")
isi = lokasi.read_text()

for baris in isi.splitlines():
    print(baris.replace("Python", "C"))