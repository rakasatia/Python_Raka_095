print("Kalkulator penjumlahan (ketik 'q' untuk berhenti)")

while True:
    angka_satu = input("\nAngka pertama: ")
    if angka_satu == "q":
        break
    angka_dua = input("Angka kedua: ")
    if angka_dua == "q":
        break

    try:
        jumlah = int(angka_satu) + int(angka_dua)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks. Coba lagi ya.")
    else:
        print(f"Hasil: {angka_satu} + {angka_dua} = {jumlah}")