from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.snake_move()

    def create_snake(self):
        for position in POSITION:
            self.add_segments(position)

    def add_segments(self, position):
        new_turtle = Turtle()
        new_turtle.color("olive")
        new_turtle.shape("square")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def snake_move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_coordinate = self.segments[seg_num - 1].xcor()
            y_coordinate = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_coordinate, y_coordinate)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
