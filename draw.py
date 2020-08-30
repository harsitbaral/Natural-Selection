import turtle
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 675

grid_size = 100

# Screen Setup
wn = turtle.Screen()
wn.tracer(0)
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.bgcolor('black')
wn.title('Natural Selection Simulator')

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

food_pen = turtle.Turtle()
food_pen.speed(0)
food_pen.shape('square')
food_pen.color('green')
food_pen.penup()

class AnimalSprite:
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
            self.move_up()
        elif selected_function == "move_down":
            self.move_down()
        elif selected_function == "move_left":
            self.move_left()
        elif selected_function == "move_right":
            self.move_right()
        elif selected_function == "move_upright":
            self.move_upright()
        elif selected_function == "move_upleft":
            self.move_upleft()
        elif selected_function == "move_downleft":
            self.move_downleft()
        elif selected_function == "move_downright":
            self.move_downleft()
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

class FoodSprite(Sprite):
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color

    def render(self, pen):
        pen.goto(self.x, self.y)
        pen.shapesize(0.5, 0.5)
        pen.shape(self.shape)
        pen.color(self.color)
        pen.stamp()

animal_sprites = []
food_sprites = []

def move_sprites():
    pen.clear()
    time.sleep(0.1)
    for sprite in animal_sprites:
        sprite.render(pen)
        sprite.update()

    wn.update()

def render_food():
    food_pen.clear()

    for food_piece in food_sprites:
        food_piece.render(food_pen)

    wn.update()
