guest_list = ["Olivia Rodrigo", "Lionel Messi", "James Arthur"]

print("Saya menemukan meja makan yang lebih besar, jadi saya akan mengundang lebih banyak tamu.")

guest_list.insert(0, "Nikola Tesla")
guest_list.insert(2, "Cristiano Ronaldo")
guest_list.append("Alan Walker")

print(f"\nHalo {guest_list[0]}, saya mengundangmu makan malam.")
print(f"Halo {guest_list[1]}, saya mengundangmu makan malam.")
print(f"Halo {guest_list[2]}, saya mengundangmu makan malam.")
print(f"Halo {guest_list[3]}, saya mengundangmu makan malam.")
print(f"Halo {guest_list[4]}, saya mengundangmu makan malam.")
print(f"Halo {guest_list[5]}, saya mengundangmu makan malam.")

print(f"\nSaya mengundang {len(guest_list)} orang untuk makan malam.")