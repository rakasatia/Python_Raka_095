peliharaan_1 = {'hewan': 'kucing', 'pemilik': 'Firman'}
peliharaan_2 = {'hewan': 'anjing', 'pemilik': 'Slamet'}
peliharaan_3 = {'hewan': 'kelinci', 'pemilik': 'Daryono'}
peliharaan_4 = {'hewan': 'burung', 'pemilik': 'Jokowi'}

hewan_peliharaan = [peliharaan_1, peliharaan_2, peliharaan_3, peliharaan_4]

for peliharaan in hewan_peliharaan:
    print(f"{peliharaan['pemilik']} memiliki seekor {peliharaan['hewan']}.")