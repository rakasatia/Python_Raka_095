pertanyaan = "\nMasukkan topping pizza yang kamu mau"
pertanyaan += "\n(ketik 'quit' kalau sudah selesai): "

topping = ""
while topping != 'quit':
    topping = input(pertanyaan)

    if topping != 'quit':
        print(f"Saya akan menambahkan {topping} ke pizzamu.")