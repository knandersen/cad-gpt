from rhino3dm import *
import math

circles = []
for i in range(10):
    angle = i*(2*math.pi/10)
    x = math.cos(angle)*10
    y = math.sin(angle)*10
    circles.append(Circle(Point3d(x, y, 0), 1+(i*2)))

model = File3dm()
for circle in circles:
    model.Objects.AddCircle(circle)

model.Write("export.3dm", 6)
