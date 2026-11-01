def cetak_desain(desain_belum_dicetak, model_selesai):
    """
    Mensimulasikan pencetakan tiap desain sampai tidak ada yang tersisa.
    Pindahkan tiap desain ke model_selesai setelah dicetak.
    """
    while desain_belum_dicetak:
        desain_sekarang = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_sekarang}")
        model_selesai.append(desain_sekarang)


def tampilkan_model_selesai(model_selesai):
    """Menampilkan semua model yang sudah dicetak."""
    print("\nModel berikut sudah dicetak:")
    for model in model_selesai:
        print(model)