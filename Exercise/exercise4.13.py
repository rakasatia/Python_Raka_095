buffet_foods = ("nasi goreng", "soto ayam", "sate ayam", "gado-gado", "rendang")

print("Menu prasmanan:")
for food in buffet_foods:
    print(food)

# Percobaan mengubah item. Baris ini sengaja dijadikan komentar
# agar program tetap jalan. Hapus tanda # untuk melihat error-nya.
# buffet_foods[0] = "bakso"
# TypeError: 'tuple' object does not support item assignment

buffet_foods = ("nasi goreng", "bakso", "sate ayam", "gado-gado", "pecel lele")

print("\nMenu prasmanan yang baru:")
for food in buffet_foods:
    print(food)