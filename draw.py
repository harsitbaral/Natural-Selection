import turtle
import random
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

grid_size = 0

# Screen Setup
wn = turtle.Screen()
wn.tracer(0)
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.bgcolor('black')
wn.title('Natural Selection Simulator')

bound = turtle.Turtle()
bound.speed(0)
bound.shape("circle")
bound.color("white")
bound.penup()
bound.goto(-360, 360)
bound.hideturtle()


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

def draw_boundaries():
    bound.pendown()
    bound.goto(360, 360)
    bound.goto(360, -360)
    bound.goto(-360, -360)
    bound.goto(-360, 360)

class AnimalSprite:
    def __init__(self, x, y, shape, color, state):
        self.shapesizex = 0.5
        self.shapesizey = 0.5
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.state = state
        self.boundary = 0

    def update(self):

        if self.y > 50:
            self.boundary == 1
        elif self.y < -50:
            self.boundary == 2
        elif self.x < -50:
            self.boundary == 3
        elif self.x > 50:
            self.boundary == 4
        elif self.x < -50 and self.y > 50:
            self.boundary == 5
        elif self.x > 50 and self.y > 50:
            self.boundary == 6
        elif self.x < -50 and self.y < -50:
            self.boundary == 7
        elif self.x > 50 and self.y < -50:
            self.boundary == 8
        else:
            self.boundary == 0


        if self.boundary == 0:
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
                self.move_downright()
            else:
                pass
        elif self.boundary == 1:
            selected_function = random.choice(["move_down","move_left", "move_right", "move_downleft","move_downright"])

            if selected_function == "move_down":
                self.move_down()
            elif selected_function == "move_left":
                self.move_left()
            elif selected_function == "move_right":
                self.move_right()
            elif selected_function == "move_downleft":
                self.move_downleft()
            elif selected_function == "move_downright":
                self.move_downright()
            else:
                pass
        elif self.boundary == 2:
            selected_function = random.choice(["move_up", "move_left", "move_right", "move_upright", "move_upleft"])

            if selected_function == "move_up":
                self.move_up()
            elif selected_function == "move_left":
                self.move_left()
            elif selected_function == "move_right":
                self.move_right()
            elif selected_function == "move_upright":
                self.move_upright()
            elif selected_function == "move_upleft":
                self.move_upleft()
            else:
                pass
        elif self.boundary == 3:
            selected_function = random.choice(["move_up", "move_down", "move_right", "move_upright", "move_downright"])

            if selected_function == "move_up":
                self.move_up()
            elif selected_function == "move_down":
                self.move_down()
            elif selected_function == "move_right":
                self.move_right()
            elif selected_function == "move_upright":
                self.move_upright()
            elif selected_function == "move_downright":
                self.move_downright()
            else:
                pass
        elif self.boundary == 4:
            selected_function = random.choice(["move_up", "move_down", "move_left", "move_upleft", "move_downleft"])

            if selected_function == "move_up":
                self.move_up()
            elif selected_function == "move_down":
                self.move_down()
            elif selected_function == "move_left":
                self.move_left()
            elif selected_function == "move_upleft":
                self.move_upleft()
            elif selected_function == "move_downleft":
                self.move_downleft()
            else:
                pass
        elif self.boundary == 5:
            selected_function = random.choice(["move_down", "move_right", "move_downright"])

            if selected_function == "move_down":
                self.move_down()
            elif selected_function == "move_right":
                self.move_right()
            elif selected_function == "move_downright":
                self.move_downright()
            else:
                pass
        elif self.boundary == 6:
            selected_function = random.choice(["move_down", "move_left", "move_downleft"])

            if selected_function == "move_down":
                self.move_down()
            elif selected_function == "move_left":
                self.move_left()
            elif selected_function == "move_downleft":
                self.move_downleft()
            else:
                pass
        elif self.boundary == 7:
            selected_function = random.choice(["move_up", "move_right", "move_upright"])

            if selected_function == "move_up":
                self.move_up()
            elif selected_function == "move_right":
                self.move_right()
            elif selected_function == "move_upright":
                self.move_upright()
            else:
                pass
        elif self.boundary == 8:
            selected_function = random.choice(["move_up", "move_left", "move_upleft"])

            if selected_function == "move_up":
                self.move_up()
            elif selected_function == "move_left":
                self.move_left()
            elif selected_function == "move_upleft":
                self.move_upleft()
            else:
                pass
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


animal_sprites = []
food_sprites = []

def move_sprites():
    pen.clear()
    time.sleep(0.1)
    for sprite in animal_sprites:
        sprite.render(pen)
        sprite.update()

    draw_boundaries()

    wn.update()


def render_food():
    food_pen.clear()

    for food_piece in food_sprites:
        food_piece.render(food_pen)

    wn.update()
