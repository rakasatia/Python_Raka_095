daftar_pengguna = ['Raka', 'Samuel', 'Fayaz', 'Nizar', 'Abraham']

for pengguna in daftar_pengguna:
    if pengguna == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {pengguna.title()}, terima kasih telah masuk kembali.")