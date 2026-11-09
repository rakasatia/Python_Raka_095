import json
from pathlib import Path

lokasi = Path("Python_Raka_095/Exercise/exercise10_13.json")

if lokasi.exists():
    data_pengguna = json.loads(lokasi.read_text())
    print("Program mengingat data berikut tentang kamu:")
else:
    data_pengguna = {
        "nama": input("Siapa namamu? "),
        "kota": input("Di kota mana kamu tinggal? "),
        "hobi": input("Apa hobimu? "),
    }
    lokasi.write_text(json.dumps(data_pengguna))
    print("Data kamu sudah disimpan. Berikut ringkasannya:")

print(f"- Nama : {data_pengguna['nama']}")
print(f"- Kota : {data_pengguna['kota']}")
print(f"- Hobi : {data_pengguna['hobi']}")