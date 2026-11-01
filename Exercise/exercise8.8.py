def buat_album(artis, judul, jumlah_lagu=None):
    """Membuat dictionary yang menggambarkan sebuah album musik."""
    album = {'artis': artis.title(), 'judul': judul.title()}
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
    return album


while True:
    print("\nMasukkan data album (ketik 'q' kapan saja untuk berhenti).")

    nama_artis = input("Nama artis: ")
    if nama_artis == 'q':
        break

    judul_album = input("Judul album: ")
    if judul_album == 'q':
        break

    album = buat_album(nama_artis, judul_album)
    print(album)