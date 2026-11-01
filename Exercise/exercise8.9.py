def cetak_pesan(pesan):
    """Mencetak setiap pesan teks dalam daftar."""
    for isi_pesan in pesan:
        print(isi_pesan)


daftar_pesan = [
    "Halo, apa kabar?",
    "Jangan lupa tugas Python hari ini.",
    "Besok kita akan belajar fungsi.",
    "Terima kasih ya informasinya !",
]

cetak_pesan(daftar_pesan)