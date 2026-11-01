pesanan_sandwich = ['tuna', 'pastrami', 'ayam', 'pastrami',
                    'telur', 'pastrami', 'keju']
sandwich_selesai = []

print("Maaf, deli kehabisan pastrami.")
while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')

while pesanan_sandwich:
    sandwich = pesanan_sandwich.pop()
    print(f"Saya sudah membuat sandwich {sandwich} pesananmu.")
    sandwich_selesai.append(sandwich)

print("\nSandwich yang sudah dibuat:")
for sandwich in sandwich_selesai:
    print(f"- sandwich {sandwich}")