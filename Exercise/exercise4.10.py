pizza_enak = ["pepperoni", "margherita", "hawaiian", "meat lovers", "quattro formaggi"]

print("Tiga item pertama dalam list adalah:")
for pizza in pizza_enak[:3]:
    print(pizza)

print("\nTiga item dari tengah list adalah:")
for pizza in pizza_enak[1:4]:
    print(pizza)

print("\nTiga item terakhir dalam list adalah:")
for pizza in pizza_enak[-3:]:
    print(pizza)