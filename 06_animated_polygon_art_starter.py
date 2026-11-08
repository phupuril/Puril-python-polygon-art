"""Animated polygon artwork: twelve colorful polygons moving in smooth orbits."""
import turtle
import random
import math
import time
from polygon_shape import Polygon

screen = turtle.Screen()
screen.setup(850, 600)
screen.title("Orbiting Polygon Art")
screen.bgcolor("black")
screen.tracer(0)

rng = random.Random(17)
colors = ["cyan", "springgreen", "orange", "deepskyblue", "plum", "yellow"]
shapes = []


for _ in range(12):
    x = rng.randint(-290, 210)
    y = rng.randint(-170, 120)
    polygon = Polygon(x, y, rng.randint(3, 6), rng.randint(35, 105),
                      rng.choice(colors), rng.randint(1, 6), rng.randint(0, 359))
    polygon.draw()
    shapes.append((polygon, x, y, rng.random() * 2 * math.pi))

for frame in range(120):
    for polygon, home_x, home_y, phase in shapes:
        x = home_x + 36 * math.cos(frame * 0.06 + phase)
        y = home_y + 26 * math.sin(frame * 0.06 + phase)
        polygon.move_to(x, y)
    screen.update()
    time.sleep(0.035)

screen.mainloop()