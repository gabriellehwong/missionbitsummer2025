import random

restaurants = [
    "Burger Palace",
    "Sushi World",
    "Pasta Heaven",
    "Taco Town",
    "Curry Express",
    "Vegan Delight"
]

def random_restaurant(list):
    random_integer = random.randint(0, len(list) - 1)
    print("Tonight's pick is:", restaurants[random_integer])

random_restaurant(restaurants)