# Write a function `describe_pet(pet_name, animal_type="dog")` that prints `"I have a dog named Bruno."` Call it three ways: with both arguments, with only the name, and with keyword arguments in reversed order.

def describe_pet(pet_name, animal_type = "dog"):
    print("I have a " + animal_type + " named " + pet_name + ".")

describe_pet("Bruno","dog")
describe_pet("Bruno")
describe_pet("dog","Bruno")

# What i learned if i dont give an argument like in 2nd call i didnt mentioned animal_type arguement it used defualt argument set in function which is dog, in 3rd function call we reversed the passed arguments so for that call it used those reversed arguments for the function rather than default ones.