pesanan_sandwich = ['tuna', 'ayam', 'telur', 'keju']
sandwich_selesai = []

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()
    print(f"Saya sudah membuat sandwich {sandwich} pesananmu.")
    sandwich_selesai.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in sandwich_selesai:
    print(f"- sandwich {sandwich}")