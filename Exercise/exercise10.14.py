import json
from pathlib import Path


def ambil_nama_tersimpan():
    lokasi = Path("Python_Raka_095/Exercise/exercise10_14.json")
    if lokasi.exists():
        return json.loads(lokasi.read_text())
    return None


def ambil_nama_baru():
    nama_pengguna = input("Siapa namamu? ")
    lokasi = Path("Python_Raka_095/Exercise/exercise10_14.json")
    lokasi.write_text(json.dumps(nama_pengguna))
    return nama_pengguna


def sapa_pengguna():
    nama_pengguna = ambil_nama_tersimpan()
    if nama_pengguna:
        jawaban = input(f"Apakah kamu {nama_pengguna}? (y/t) ")
        if jawaban.lower() == "y":
            print(f"Selamat datang kembali, {nama_pengguna}!")
        else:
            nama_pengguna = ambil_nama_baru()
            print(f"Kami akan mengingatmu, {nama_pengguna}!")
    else:
        nama_pengguna = ambil_nama_baru()
        print(f"Kami akan mengingatmu, {nama_pengguna}!")


sapa_pengguna()