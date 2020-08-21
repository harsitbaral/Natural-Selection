import random
import draw


class GridX:
    def __init__(self, x, number):
        self.x = x
        self.number = number

    def Render(self):
        pass


class GridY:
    def __init__(self, y, number):
        self.y = y
        self.number = number


class Animal:
    def __init__(self, x, y, energy, e_consump, speed, sight, color, shape):
        self.speed(0)
        self.x = x
        self.y = y
        self.energy = energy
        self.e_consump = e_consump
        self.speed = speed
        self.sight = sight


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y


number_of_animals = int(input('Enter the number of animals: '))

starting_food_range = int(input("Starting food range:"))
ending_food_range = int(input("\nEnding food range: "))

number_of_food = random.randint(starting_food_range, ending_food_range)

# animals = {}
animal_x = 0
animal_y = 0
animal_energy = 0
animal_speed = 1
animal_e_consump = 0  # Round it
animal_sight = 1
generation = 1
animal_color = ""
animal_shape = ""


def InitalizeAnimals():
    for i in range(number_of_animals):
        animal_x = random.randint(0, draw.grid_size)
        animal_y = random.randint(0, draw.grid_size)
        animal_e_consump = (animal_speed + animal_sight) ** 1.5
        animal = Animal(animal_x, animal_y, animal_energy, animal_e_consump,
                        animal_speed, animal_sight, animal_color, animal_shape)
        # animals.append(f"animal{i}")


def NewRound():
    InitalizeAnimals()


def Reproduce(animal, generation):
    generation += 1
    # The speed is on a bell curve based on its parents speed
    # Same with sight


def Die():
    pass
