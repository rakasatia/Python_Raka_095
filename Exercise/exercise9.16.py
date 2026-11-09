
import random

print("=== Python Module of the Week: random ===")

# 1. random(): menghasilkan angka desimal acak
print("\n1. Fungsi random()")
angka_acak = random.random()
print(f"Angka desimal acak: {angka_acak}")


# 2. uniform(): menghasilkan angka desimal dalam rentang tertentu
print("\n2. Fungsi uniform()")
angka_rentang = random.uniform(1, 10)
print(f"Angka acak antara 1 dan 10: {angka_rentang}")


# 3. randint(): menghasilkan bilangan bulat acak
print("\n3. Fungsi randint()")
angka_dadu = random.randint(1, 6)
print(f"Hasil lemparan dadu: {angka_dadu}")


# 4. choice(): memilih satu elemen secara acak
print("\n4. Fungsi choice()")
buah = ["apel", "jeruk", "mangga", "pisang"]
buah_terpilih = random.choice(buah)
print(f"Buah yang terpilih: {buah_terpilih}")
