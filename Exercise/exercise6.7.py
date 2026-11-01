orang_1 = {'first_name': 'Raka', 'last_name': 'Pratama',
            'age': 25, 'city': 'Semarang'}
orang_2 = {'first_name': 'Bambang', 'last_name': 'Sugianto',
            'age': 22, 'city': 'Bandung'}
orang_3 = {'first_name': 'Slamet', 'last_name': 'Riyanto',
            'age': 30, 'city': 'Surabaya'}

people = [orang_1, orang_2, orang_3]

for orang in people:
    for key, value in orang.items():
        print(f"{key}: {value}")
    print()