menu_prasmanan = ("nasi goreng", "soto ayam", "sate ayam", "gado-gado", "rendang")

print("Menu prasmanan:")
for makanan in menu_prasmanan:
    print(makanan)

# Percobaan mengubah item. Baris ini sengaja dijadikan komentar
# agar program tetap jalan. Hapus tanda # untuk melihat error-nya.
# menu_prasmanan[0] = "bakso"
# TypeError: 'tuple' object does not support item assignment

menu_prasmanan = ("nasi goreng", "bakso", "sate ayam", "gado-gado", "pecel lele")

print("\nMenu prasmanan yang baru:")
for makanan in menu_prasmanan:
    print(makanan)