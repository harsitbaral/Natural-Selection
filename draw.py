# Green = Reproduce
# Black = Die
# White = Live


import turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 675

# Screen Setup
wn = turtle.Screen()
wn.tracer(0)
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.bgcolor('black')
wn.title('Natural Selection Simulator')

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
grid_size = 100

class Animal:
	def __init__(self, x, y, shape, color):
		self.x = x
		self.y = y
		self.shape = shape
		self.color = color
		self.dx = 0
		self.dy = 0

	def update(self):
		self.x += self.dx
		self.y += self.dy

	def render(self, pen):
		pen.goto(self.x, self.y)
		pen.shape(self.shape)
		pen.color(self.color)
		pen.stamp()


animal_one = Animal(0, 0, 'turtle', 'white')
animal_one.dx = 0
animal_one.dy = 0

animals = []
animals.append(animal_one)


while True:
	pen.clear()

	for animal in animals:
		animal.render(pen)
	wn.update()
