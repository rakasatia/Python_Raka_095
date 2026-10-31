kota = {
    'tokyo': {
        'negara': 'jepang',
        'bahasa': 'Jepang',
        'population': 14000000,
        'fakta': 'dulu bernama Edo sebelum tahun 1868.',
    },
    'paris': {
        'negara': 'prancis',
        'bahasa': 'Prancis',
        'populasi': 2100000,
        'fakta': 'Menara Eiffel selesai dibangun pada tahun 1889.',
    },
    'kairo': {
        'negara': 'mesir',
        'bahasa': 'Arab',
        'populasi': 10000000,
        'fakta': 'berada dekat dengan Piramida Giza.',
    },
}

for city, info in kota.items():
    populasi = f"{info['populasi']:,}".replace(',', '.')
    print(f"\n{city.title()}")
    print(f"  Negara   : {info['negara'].title()}")
    print(f"  Bahasa   : {info['bahasa']}")
    print(f"  Populasi : sekitar {populasi} jiwa")
    print(f"  Fakta    : {info['fakta']}")