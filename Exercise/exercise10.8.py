from pathlib import Path

nama_berkas = ["Python_Raka_095/Exercise/exercise10.8a.txt", "Python_Raka_095/Exercise/exercise10.8b.txt"]

for nama in nama_berkas:
    lokasi = Path(nama)
    try:
        isi = lokasi.read_text()
    except FileNotFoundError:
        print(f"Maaf, file {nama} tidak ditemukan.")
    else:
        print(f"Isi file {nama}:")
        print(isi)