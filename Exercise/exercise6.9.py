favorite_places = {
    'amri': ['Bali', 'Yogyakarta'],
    'ricko': ['Raja Ampat', 'Bandung', 'Malang'],
    'dewok': ['Labuan Bajo'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")