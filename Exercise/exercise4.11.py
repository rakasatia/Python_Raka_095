pizza_saya= ["pepperoni", "margherita", "hawaiian"]
pizza_teman = pizza_saya[:]

pizza_saya.append("meat lovers")
pizza_teman.append("quattro formaggi")

print("Pizza favoritku adalah:")
for pizza in pizza_saya:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in pizza_teman:
    print(pizza)