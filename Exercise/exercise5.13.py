# Jadi, ide saya adalah mencoba membuat report untuk diri sendiri tentang nilai-nilai yang saya dapatkan di beberapa mata kuliah.

daftar_matkul = ['Matematika', 'Bahasa Indonesia', 'Fisika', 'Bahasa Inggris', 'Kimia']
daftar_nilai = [85, 98, 92, 93,90]
mapel_wajib = ['Matematika', 'Kimia', 'Fisika']

if daftar_nilai:
    total = sum(daftar_nilai)
    rata_rata = total / len(daftar_nilai)
    nilai_tertinggi = max(daftar_nilai)
    nilai_terendah = min(daftar_nilai)

    print("=== Laporan Nilai ===")
    print(f"Total: {total}")
    print(f"Rata-rata: {rata_rata}")
    print(f"Tertinggi: {nilai_tertinggi}")
    print(f"Terendah: {nilai_terendah}")

    print("\n=== Predikat Tiap Matkul ===")
    for nomor in range(len(daftar_nilai)):
        nama_matkul = daftar_matkul[nomor]
        nilai = daftar_nilai[nomor]

        if nilai >= 85:
            predikat = 'A'
        elif nilai >= 75:
            predikat = 'B'
        elif nilai >= 65:
            predikat = 'C'
        else:
            predikat = 'D'
        print(f"{nama_matkul}: {nilai} -> {predikat}")

    
        if nilai == nilai_tertinggi:
            print("   ^ Nilai tertinggi!")
        if nilai == nilai_terendah:
            print("   ^ Nilai terendah, perlu ditingkatkan")

    # Mengecek item dengan in dan not in (seperti latihan 5-10)
    print("\n=== Cek  Wajib ===")
    daftar_matkul_kecil = []
    for nama_matkul in daftar_matkul:
        daftar_matkul_kecil.append(nama_matkul)

    for wajib in mapel_wajib:
        if wajib in daftar_matkul_kecil:
            print(f" wajib '{wajib}' ada di daftar.")
        else:
            print(f" wajib '{wajib}' TIDAK ada di daftar.")

    if 'seni' not in mapel_wajib:
        print("Catatan: Seni bukan mapel wajib.")

    print("\n=== Hasil Akhir ===")
    if nilai_terendah != nilai_tertinggi:
        print("Nilai bervariasi (tertinggi dan terendah berbeda).")

    sudah_lulus = rata_rata >= 70 and nilai_terendah >= 60
    print(f"Lulus? {sudah_lulus}")

    if sudah_lulus:
        print("Status: LULUS")
    elif rata_rata >= 70 or nilai_terendah >= 60:
        print("Status: REMEDIAL (ada syarat yang belum terpenuhi)")
    else:
        print("Status: TIDAK LULUS")
else:
    print("Belum ada nilai yang bisa diproses!")