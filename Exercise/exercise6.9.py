tempat_favorit = {
    'amri': ['Banda Neira', 'Yogyakarta'],
    'ricko': ['Raja Ampat', 'Bandung', 'Malang'],
    'dewok': ['Labuan Bajo'],
}

for name, places in tempat_favorit.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")