import draw

import random
from datetime import datetime, timedelta
import scipy.stats
import numpy as np

# number_of_animals = int(input('Enter the number of animals: '))
number_of_animals = 50

# starting_food_range = int(input("Starting food range:"))
starting_food_range = 25

# ending_food_range = int(input("\nEnding food range: "))
ending_food_range = 35

number_of_food = random.randint(starting_food_range, ending_food_range)

animal_x = 0
animal_y = 0
animal_energy = 0
animal_speed = 1
animal_e_consump = 0  # Round it
animal_sight = 1
generation = 1
animal_color = "white"
animal_shape = "turtle"
animal_state = ""
animals = []
food_pieces = []

class Animal:
    def __init__(self, x, y, speed, sight, color, shape):
        self.speed = 1
        self.x = x
        self.y = y
        self.energy = 0
        self.e_consump = 0
        self.speed = speed
        self.sight = sight
        self.state = 'n'
        self.color = color
        self.shape = shape
        # n = none, d = dead, r = reproducing, a = alive

class Food:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

# def create_bell_curve(start, end):
#     # Start at length/2 - 1 tenth of length
#     mean = end/2
#     standard_deviation = 1
#
#     x_values = np.arange(start, end, 1)
#     y_values = scipy.stats.norm(mean, standard_deviation)
#     return y_values.pdf(x_values)


def InitalizeAnimals():
    for i in range(number_of_animals):
        animal_x = random.randint(0, draw.grid_size)
        animal_y = random.randint(0, draw.grid_size)
        animal_e_consump = (animal_speed + animal_sight) ** 1.5

        animal = Animal(animal_x, animal_y, animal_speed, animal_sight, animal_color, animal_shape)

        animals.append(animal)
        animal = draw.AnimalSprite(animal_x, animal_y, animal_shape, animal_color, animal_state)
        draw.animal_sprites.append(animal)

def InitializeFood():
    for i in range(number_of_food):
        food_x = random.randint(0, draw.grid_size)
        food_y = random.randint(0, draw.grid_size)
        food_colour = "red"

        new_food = Food(food_x, food_y, food_colour)
        food_pieces.append(new_food)
        new_food = draw.FoodSprite(food_x, food_x, food_colour)
        draw.food_sprites.append(new_food)
    draw.render_food()

def check_bounderies():
    pass


def move_animals():
    for i in range(100000): # TODO Change this to a timer
        # Move animal
        draw.move_sprites()

def NewRound():
    InitalizeAnimals()
    move_animals()

print("starting up simulation")
NewRound()

# def Reproduce(animal):
#     global generation
#     generation += 1
#     # The speed is on a bell curve based on its parents speed
#     speed_curve = create_bell_curve(animal.speed, animal.speed * 1.5)
#     # Same with sight
#     sight_curve = create_bell_curve(animal.sight, animal.sight * 2)
#
#     speed = random.choice(speed_curve) / 20
#     sight = random.choice(sight_curve) / 20
#
#     animal = Animal(animal_x, animal_y, speed, sight, animal_color, animal_shape)
#
#     return animal

# def Die():
#     pass
