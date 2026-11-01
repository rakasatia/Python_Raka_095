def membuat_profil(nama_depan, nama_belakang, **info_pengguna):
    """Membuat dictionary yang berisi semua yang kita ketahui tentang pengguna."""
    profil = {
        'nama_depan': nama_depan,
        'nama_belakang': nama_belakang,
    }
    for kunci, nilai in info_pengguna.items():
        profil[kunci] = nilai
    return profil


profil_saya = membuat_profil(
    'Raka', 'Pratama',
    kampus='UNS',
    jurusan='Teknik Industri',
    hobi='main gitar',
)
print(profil_saya)