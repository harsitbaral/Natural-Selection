import turtle
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

grid_size = 800

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

class AnimalSprite:
    def __init__(self, x, y, shape, color, state):
        self.shapesizex = 0.5
        self.shapesizey = 0.5
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.state = state

        self.right_counter = 0
        self.left_counter = 0

        self.up_counter = 0
        self.down_counter = 0

        self.ur_counter = 0
        self.ul_counter = 0

        self.dr_counter = 0
        self.dl_counter = 0

    def update(self):
        choices = ["move_up", "move_down", "move_left", "move_right", "move_upright", "move_upleft", "move_downleft", "move_downright"]
        selected_function = random.randint(0, 8)

        if selected_function == 0:
            self.move_up()
        elif selected_function == 1:
            self.move_down()
        elif selected_function == 2:
            self.move_left()
        elif selected_function == 3:
            self.move_right()
        elif selected_function == 4:
            self.move_upright()
        elif selected_function == 5:
            self.move_upleft()
        elif selected_function == 6:
            self.move_downleft()
        elif selected_function == 7:
            self.move_downright()
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
        self.up_counter += 1

    def move_down(self):
        self.y -= 10
        self.down_counter += 1

    def move_left(self):
        self.x -= 10
        self.left_counter += 1

    def move_right(self):
        self.x += 10
        self.right_counter += 1

    def move_upright(self):
        self.move_up()
        self.move_right()
        self.ur_counter += 1

    def move_upleft(self):
        self.move_up()
        self.move_left()
        self.ul_counter += 1

    def move_downright(self):
        self.move_down()
        self.move_right()
        self.dr_counter += 1

    def move_downleft(self):
        self.move_down()
        self.move_left()
        self.dl_counter += 1

class FoodSprite:
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
        print("RIGHT: " + str(sprite.right_counter))
        print("LEFT: " + str(sprite.left_counter))
        print("UP: " + str(sprite.up_counter))
        print("DOWN: " + str(sprite.down_counter))
        print("UP_RIGHT: " + str(sprite.ur_counter))
        print("UP_LEFT: " + str(sprite.ul_counter))
        print("DOWN_RIGHT: " + str(sprite.dr_counter))
        print("DOWN_LEFT: " + str(sprite.dl_counter))

    wn.update()

def render_food():
    pen.clear()

    for food_piece in food_sprites:
        food_piece.render(pen)

    wn.update()