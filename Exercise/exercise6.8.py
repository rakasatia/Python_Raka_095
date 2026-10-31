pet_1 = {'hewan': 'kucing', 'pemilik': 'Firman'}
pet_2 = {'hewan': 'anjing', 'pemilik': 'Slamet'}
pet_3 = {'hewan': 'kelinci', 'pemilik': 'Daryono'}
pet_4 = {'hewan': 'burung', 'pemilik': 'Jokowi'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"{pet['pemilik']} memiliki seekor {pet['hewan']}.")