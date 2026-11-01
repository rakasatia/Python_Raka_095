hasil_polling = {}

polling_aktif = True
while polling_aktif:
    nama = input("\nSiapa namamu? ")
    tempat = input(
        "Jika kamu bisa mengunjungi satu tempat di dunia, "
        "ke mana kamu akan pergi? "
    )

    hasil_polling[nama] = tempat

    ulang = input("Apakah ada orang lain yang mau ikut polling? (ya/tidak) ")
    if ulang == 'tidak':
        polling_aktif = False

print("\n--- Hasil Polling ---")
for nama, tempat in hasil_polling.items():
    print(f"{nama.title()} ingin berlibur ke {tempat.title()}.")