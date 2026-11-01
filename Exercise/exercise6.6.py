favorite_languages = {
    'Raka': 'python',
    'Bambang': 'c',
    'Jamal': 'rust',
    'Suwandi': 'python',
}

list_orang = ['Raka', 'Bambang', 'Jamal', 'Suwandi', 'Revano']

for orang in list_orang:
    if orang in favorite_languages:
        print(f"Terima kasih {orang.title()} sudah mengisi polling!")
    else:
        print(f"{orang.title()}, maukah kamu mengisi polling bahasa favorit?")