guest_list = ["Olivia Rodrigo", "Lionel Messi", "James Arthur", "Nikola Tesla", "Cristiano Ronaldo", "Alan Walker"]

print("Maaf, meja makan malam tidak tiba tepat waktu. Saya hanya bisa mengundang dua orang.")

removed_guest = guest_list.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundangmu makan malam.")

removed_guest = guest_list.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundangmu makan malam.")

removed_guest = guest_list.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundangmu makan malam.")

removed_guest = guest_list.pop()
print(f"Maaf {removed_guest}, saya tidak bisa mengundangmu makan malam.")

print(f"\nHalo {guest_list[0]}, kamu masih diundang makan malam.")
print(f"Halo {guest_list[1]}, kamu masih diundang makan malam.")

del guest_list[-1]
del guest_list[-1]

print(guest_list)