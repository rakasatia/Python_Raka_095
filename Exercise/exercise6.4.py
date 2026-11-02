glosarium = {
    'variable': 'nama yang menyimpan sebuah nilai.',
    'string': 'rangkaian karakter yang diapit tanda kutip.',
    'list': 'kumpulan item berurutan dalam kurung siku.',
    'loop': 'perulangan yang menjalankan kode berkali-kali.',
    'comment': 'catatan di dalam kode yang diabaikan Python.',
    'tuple': 'kumpulan item berurutan yang isinya tidak bisa diubah.',
    'dictionary': 'kumpulan pasangan key-value dalam kurung kurawal.',
    'function': 'blok kode bernama yang bisa dipanggil berulang kali.',
    'parameter': 'variabel di definisi fungsi yang menerima nilai.',
    'slice': 'potongan sebagian dari sebuah list.',
}

for kata, arti in glosarium.items():
    print(f"{kata}:\n\t{arti}\n")