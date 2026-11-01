pertanyaan = "\nMasukkan topping pizza yang kamu mau"
pertanyaan += "\n(ketik 'quit' kalau sudah selesai): "

while True:
    topping = input(pertanyaan)

    if topping == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizzamu.")