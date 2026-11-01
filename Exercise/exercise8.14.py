def membuat_mobil(pabrikan, model, **fitur):
    """Membuat dictionary yang berisi informasi sebuah mobil."""
    mobil = {
        'pabrikan': pabrikan,
        'model': model,
    }
    for kunci, nilai in fitur.items():
        mobil[kunci] = nilai
    return mobil


mobil = membuat_mobil('subaru', 'outback', warna='biru', paket_derek=True)
print(mobil)