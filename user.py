from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

#This class for creating the object turtle
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(2, 2, 6)
        self.color("black", "#FF5733")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.pendown()
        self.steps_remaining = 0  # for smooth movement
        self.pensize(4)  # thickness of the trail
        self.pencolor("#FF5733")

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.pendown()
        self.forward(90) #move upward

    #to decrease the speed
    def _move_step(self, speed):
        if self.steps_remaining > 0:
            self.forward(speed)
            self.steps_remaining -= speed
            self.screen.update()  # needed if tracer(0)
            self.screen.ontimer(lambda: self._move_step(speed), 200)  # delay in ms


#To make the turtle blink when moving and replying to questions
    def disco_blink(self, flashes=6, delay=120):
        colors = ["yellow", "cyan", "magenta", "lime", "white", "deepskyblue", "hotpink"]

        def blink_cycle(count):
            if count > 0:
                new_color = colors[count % len(colors)]
                self.fillcolor(new_color)
                self.showturtle() if not self.isvisible() else self.hideturtle()
                self.screen.update()
                self.screen.ontimer(lambda: blink_cycle(count - 1), delay)
            else:
                self.showturtle()
                self.color("#FF5733")  # reset to original color
                self.pencolor("#FF5733")
                self.screen.update()

        blink_cycle(flashes * 2)  # each flash is a show/hide


#This class is to create the aim point, visually a square
class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#f6e3ab")
        self.shapesize(1, 2)
        self.penup()
        self.goto(0,180)


#The aim line created by drawing the line with a turtle object
class DrawLine(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("#f6e3ab")
        self.hideturtle()
        self.penup()
        self.goto(-200, 180)
        self.setheading(0)  # Face right (0 degrees)
        self.pensize(5)
        self.pendown()

    def drawline(self):
        self.forward(400)  # Draws horizontal line to the right


