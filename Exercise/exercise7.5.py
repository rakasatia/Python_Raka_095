pertanyaan = "\nBerapa umurmu? (ketik 'quit' untuk berhenti) "

while True:
    umur = input(pertanyaan)

    if umur == 'quit':
        break

    umur = int(umur)

    if umur < 3:
        print("Tiketmu gratis.")
    elif umur <= 12:
        print("Harga tiketmu $10.")
    else:
        print("Harga tiketmu $15.")