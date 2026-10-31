person_1 = {'first_name': 'Raka', 'last_name': 'Pratama',
            'age': 25, 'city': 'Semarang'}
person_2 = {'first_name': 'Bambang', 'last_name': 'Sugianto',
            'age': 22, 'city': 'Bandung'}
person_3 = {'first_name': 'Slamet', 'last_name': 'Riyanto',
            'age': 30, 'city': 'Surabaya'}

people = [person_1, person_2, person_3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print()