def kota_negara(kota, negara):
    """Mengembalikan nama kota dan negara dalam satu string."""
    return f"{kota.title()}, {negara.title()}"


hasil_1 = kota_negara('santiago', 'chile')
hasil_2 = kota_negara('yogyakarta', 'indonesia')
hasil_3 = kota_negara('kyoto', 'jepang')

print(hasil_1)
print(hasil_2)
print(hasil_3)