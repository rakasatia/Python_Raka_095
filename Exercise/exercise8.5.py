def deskripsi_kota(kota, negara='Indonesia'):
    """Mencetak kalimat sederhana tentang lokasi sebuah kota."""
    print(f"{kota.title()} berada di {negara.title()}.")


deskripsi_kota('yogyakarta')
deskripsi_kota('bandung')
deskripsi_kota('seattle', 'amerika serikat')