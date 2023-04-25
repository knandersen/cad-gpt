from rhino3dm import *
import math

center_pt = Point3d(0, 0, 0)
radius = 10
angle = 360/8

circles = []

for i in range(8):
    angle_rad = math.radians(angle*i)
    x = center_pt.X + radius*math.cos(angle_rad)
    y = center_pt.Y + radius*math.sin(angle_rad)
    pt = Point3d(x, y, 0)
    circles.append(Circle(pt, radius))

model = File3dm()

for circle in circles:
    model.Objects.AddCircle(circle)

model.Write("circles.3dm", 6)
