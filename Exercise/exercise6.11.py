kota = {
    'tokyo': {
        'negara': 'jepang',
        'populasi': 14000000,
        'fakta': 'dulu bernama Edo sebelum tahun 1868.',
    },
    'paris': {
        'negara': 'prancis',
        'populasi': 2100000,
        'fakta': 'Menara Eiffel selesai dibangun pada tahun 1889.',
    },
    'kairo': {
        'negara': 'mesir',
        'populasi': 10000000,
        'fakta': 'berada dekat dengan Piramida Giza.',
    },
}

for city, info in kota.items():
    print(f"\n{city.title()}")
    print(f"  Negara: {info['negara'].title()}")
    print(f"  Perkiraan populasi: {info['populasi']}")
    print(f"  Fakta: {info['fakta']}")