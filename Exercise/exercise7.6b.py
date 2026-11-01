pertanyaan = "\nMasukkan topping pizza yang kamu mau"
pertanyaan += "\n(ketik 'quit' kalau sudah selesai): "

aktif = True
while aktif:
    topping = input(pertanyaan)

    if topping == 'quit':
        aktif = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizzamu.")