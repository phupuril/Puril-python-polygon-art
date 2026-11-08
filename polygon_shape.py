"""A regular polygon that can draw and move using its own turtle."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store polygon properties and create a separate drawing turtle."""
        if sides < 3:
            raise ValueError("sides must be at least 3")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")

        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(0)

    def draw(self):
        """Draw the regular polygon from its first vertex."""
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.setheading(self.angle)
        self.t.pencolor(self.color)
        self.t.pensize(self.pen_size)
        self.t.pendown()
        for _ in range(self.sides):
            self.t.forward(self.side_length)
            self.t.left(360 / self.sides)
        self.t.penup()

    def move_to(self, x, y):
        """Move this polygon without clearing drawings by other turtles."""
        self.x = x
        self.y = y
        self.t.clear()
        self.draw()
