makanan_saya = ["pizza", "falafel", "carrot cake"]
makanan_teman = makanan_saya[:]

makanan_saya.append("cannoli")
makanan_teman.append("ice cream")

print("Makanan favoritku adalah:")
for food in makanan_saya:
    print(food)

print("\nMakanan favorit temanku adalah:")
for food in makanan_teman:
    print(food)