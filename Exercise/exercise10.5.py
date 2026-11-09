from pathlib import Path

daftar_nama = []

print("Buku Tamu (ketik 'q' kapan saja untuk berhenti)")
while True:
    nama = input("Siapa namamu? ")
    if nama == "q":
        break
    daftar_nama.append(nama)
    print(f"Terima kasih, {nama}!")

lokasi = Path("Python_Raka_095/Exercise/exercise10_5.txt")
lokasi.write_text("\n".join(daftar_nama))
print(f"{len(daftar_nama)} nama disimpan di {lokasi}.")