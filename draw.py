import turtle
import random
import time

import main

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 675

# Screen Setup
wn = turtle.Screen()
wn.tracer(0)
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.bgcolor('black')
wn.title('Natural Selection Simulator')

grid = turtle.Turtle()
grid.shape('square')
grid.color('white')
grid.speed(0)
grid.hideturtle()
grid_size = 100


def square():
    x = 0
    y = 0
    for i in range(10):
        grid.forward(50)
        grid.left(90)
        grid.forward(50)
        grid.left(90)
        grid.forward(50)
        grid.left(90)
        grid.forward(50)
        grid.left(90)
        grid.goto(50 + x, 0)
    grid.goto(0, -50)
    grid.right(90)


legend = turtle.Turtle()
legend.speed(0)
legend.shape('square')
legend.color('white')
legend.penup()
legend.hideturtle()
legend.goto(-380, 270)
legend.write("Legend:\nGreen = Reproduce\nBlack = Dies\nWhite = Lives", move=False, align="left")

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()


class Sprite:
    def __init__(self, x, y, shape, color, state):
        self.shapesizex = 0.5
        self.shapesizey = 0.5
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.state = state

    def update(self):
        selected_function = random.choice(["move_up", "move_down", "move_left", "move_right", "move_upright", "move_upleft", "move_downleft", "move_downright"])

        if selected_function == "move_up":
            sprite.move_up()
        elif selected_function == "move_down":
            sprite.move_down()
        elif selected_function == "move_left":
            sprite.move_left()
        elif selected_function == "move_right":
            sprite.move_right()
        elif selected_function == "move_upright":
            sprite.move_upright()
        elif selected_function == "move_upleft":
            sprite.move_upleft()
        elif selected_function == "move_downleft":
            sprite.move_downleft()
        elif selected_function == "move_downright":
            sprite.move_downleft()
        else:
            pass

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.shapesize(self.shapesizex, self.shapesizey)
        pen.stamp()

    def move_up(self):
        self.y += 10

    def move_down(self):
        self.y -= 10

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_upright(self):
        self.move_up()
        self.move_right()

    def move_upleft(self):
        self.move_up()
        self.move_left()

    def move_downright(self):
        self.move_down()
        self.move_right()

    def move_downleft(self):
        self.move_down()
        self.move_left()


thing_one = Sprite(0, 0, 'turtle', 'white', 'dead')

sprites = []
sprites.append(thing_one) # TODO Implement this with main

for i in range(main.number_of_animals):
    pass

while True:

    time.sleep(0.5)

    pen.clear()

    for sprite in sprites:
        sprite.render(pen)
        sprite.update()

    wn.update()