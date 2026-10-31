angka_favorit = {
    'Alex': [7, 13],
    'Bayu': [3],
    'Cika': [21, 5, 8],
    'Renaldi': [9, 18],
    'Zara': [14, 2, 42],
}

for name, numbers in angka_favorit.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(f"- {number}")