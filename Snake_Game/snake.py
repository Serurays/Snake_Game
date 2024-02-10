from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.squares = []
        self.f_y = 0
        self.f_x = 0
        self.create_snake(3)
        self.head = self.squares[0]

    def create_snake(self, num):
        for i in range(num):
            s = Turtle()
            s.shape("square")
            s.color("white")
            s.penup()
            s.sety(self.f_y)
            s.setx(self.f_x)
            self.f_x -= 20
            self.squares.append(s)

        for square in self.squares:
            square.showturtle()

    def move(self):
        for i in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[i - 1].xcor()
            new_y = self.squares[i - 1].ycor()
            self.squares[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.create_snake(1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
