pizzas = ["pepperoni", "margherita", "hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append("meat lovers")
friend_pizzas.append("quattro formaggi")

print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)