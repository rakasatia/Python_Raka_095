pengguna_saat_ini = ['Raka', 'Rafli', 'Darren', 'Samsul', 'Dewa']
pengguna_baru = ['Samuel', 'Gibran', 'Kaesang', 'Heri', 'Yonata']

pengguna_saat_ini_kecil = []
for pengguna in pengguna_saat_ini:
    pengguna_saat_ini_kecil.append(pengguna.lower())

for pengguna_baru_item in pengguna_baru:
    if pengguna_baru_item.lower() in pengguna_saat_ini_kecil:
        print(f"Nama '{pengguna_baru_item}' sudah dipakai. Silakan masukkan nama pengguna lain.")
    else:
        print(f"Nama '{pengguna_baru_item}' tersedia.")