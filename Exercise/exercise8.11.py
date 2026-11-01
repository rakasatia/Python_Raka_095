def kirim_pesan(pesan, pesan_terkirim):
    """Mencetak tiap pesan lalu memindahkannya ke daftar pesan terkirim."""
    while pesan:
        pesan_sekarang = pesan.pop(0)
        print(f"Mengirim pesan: {pesan_sekarang}")
        pesan_terkirim.append(pesan_sekarang)


daftar_pesan = [
    "Halo, apa kabar?",
    "Jangan lupa tugas Python hari ini.",
    "Besok kita kumpul jam 8 untuk belajar fungsi.",
    "Terima kasih ya!",
]
pesan_terkirim = []

kirim_pesan(daftar_pesan[:], pesan_terkirim)

print("\nDaftar pesan:", daftar_pesan)
print("Daftar pesan terkirim:", pesan_terkirim)