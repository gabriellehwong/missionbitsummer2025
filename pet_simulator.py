class Pet:
    def __init__(self, name = "", animal_type = "", hunger = 0, happiness = 100):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.happiness = happiness
    def eat(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print(f"\nHunger: {self.hunger}")
    def play(self):
        self.happiness += 10
        self.hunger += 5
        if self.happiness > 100:
            self.happiness = 100
        print(f"\nHappiness: {self.happiness}")
    def status(self):
        print(f"\nName: {self.name}")
        print(f"Type: {self.animal_type}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")

my_pet = Pet("Buddy", "Dog")

my_pet.status()
my_pet.eat()
my_pet.play()
my_pet.status()

pets = []
num_pets = int(input("\nHow many pets do you want to create? "))
for i in range(num_pets):
    print(f"\nPet #{i + 1}:")
    name = input("What’s the pet’s name? ")
    animal_type = input("What type of animal is it? ")
    pet = Pet(name, animal_type)
    pets.append(pet)

while True:
    print("What would you like to do?\n1. Feed a pet\n2. Play with a pet\n3. Check a pet's status\n4. Exit")
    input = input("Choose an action by entering a number: ")