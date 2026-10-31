favorite_languages = {
    'Raka': 'python',
    'Bambang': 'c',
    'Jamal': 'rust',
    'Suwandi': 'python',
}

people = ['Raka', 'Bambang', 'Jamal', 'Suwandi', 'Revano']

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()} sudah mengisi polling!")
    else:
        print(f"{person.title()}, maukah kamu mengisi polling bahasa favorit?")