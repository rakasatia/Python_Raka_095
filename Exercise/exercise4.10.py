pizzas = ["pepperoni", "margherita", "hawaiian", "meat lovers", "quattro formaggi"]

print("Tiga item pertama dalam list adalah:")
for pizza in pizzas[:3]:
    print(pizza)

print("\nTiga item dari tengah list adalah:")
for pizza in pizzas[1:4]:
    print(pizza)

print("\nTiga item terakhir dalam list adalah:")
for pizza in pizzas[-3:]:
    print(pizza)