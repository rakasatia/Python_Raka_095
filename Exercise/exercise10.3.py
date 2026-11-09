from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_3.txt")
print(lokasi.read_text().rstrip())

print()

lokasi = Path("Python_Raka_095/Exercise/exercise10_3.txt")
for baris in lokasi.read_text().splitlines():
    print(baris)

print()

lokasi = Path("Python_Raka_095/Exercise/exercise10_3.txt")
string_pi = ""
for baris in lokasi.read_text().splitlines():
    string_pi += baris.lstrip()

print(string_pi)
print(len(string_pi))

print()

lokasi = Path("Python_Raka_095/Exercise/exercise10_3.txt")
string_pi = ""
for baris in lokasi.read_text().splitlines():
    string_pi += baris.lstrip()

print(f"{string_pi[:52]}...")
print(len(string_pi))

print()

ulang_tahun = input("Masukkan tanggal lahirmu, dalam bentuk hhbbtt: ")
if ulang_tahun in string_pi:
    print("Tanggal lahirmu muncul dalam sejuta digit pertama pi!")
else:
    print("Tanggal lahirmu tidak muncul dalam sejuta digit pertama pi.")