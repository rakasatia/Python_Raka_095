def buat_album(artis, judul, jumlah_lagu=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {'artis': artis.title(), 'judul': judul.title()}
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
    return album


album_1 = buat_album('olivia rodrigo', 'happier')
album_2 = buat_album('the beatles', 'abbey road', jumlah_lagu=17)
album_3 = buat_album('james arthur', 'a year ago')

print(album_1)
print(album_2)
print(album_3)