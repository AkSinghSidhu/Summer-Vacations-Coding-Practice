#Write a function `make_sandwich(*fillings)` that prints each filling on its own line. Then write `order_pizza(size, *toppings, **extras)` that prints the size, all toppings, and all extra info (crust type, delivery, etc). Call it with at least 3 toppings and 2 extras.

def make_sandwich(*fillings):
    print(*fillings, sep= "\n")

def order_pizza(size, *toppings, **extras):
    print("Size of Pizza: " + size + " with the Toppings: " + ', '.join(toppings) + " and Extras: " + ", ".join(f"{k}={v}" for k, v in extras.items()))

make_sandwich("Ricotta cheese", "Ground sausage", "Spinach", "Garlic")

order_pizza("Medium", "Pepperoni", "Sliced Bell Peppers", "Red Onion", "Fresh Basil", "Mushrooms", crustType = "Crunchy", delivery = "Fast")