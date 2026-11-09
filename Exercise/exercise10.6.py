print("Program penjumlahan dua angka")

try:
    angka_satu = input("Angka pertama: ")
    angka_satu = int(angka_satu)
    angka_dua = input("Angka kedua: ")
    angka_dua = int(angka_dua)
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    jumlah = angka_satu + angka_dua
    print(f"Hasil: {angka_satu} + {angka_dua} = {jumlah}")