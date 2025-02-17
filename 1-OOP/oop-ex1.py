## Code Exercise 1 - Circle Math
import math

class Circle:
  def __init__(self, radius):
    self.radius = radius
  
  def area(self):
    return math.pi * self.radius ** 2
  
  def circumference(self):
    return 2 * math.pi * self.radius
  
  def diameter(self):
    return 2 * self.radius

circle1 = Circle(3)
print(circle1.area())
print(circle1.circumference())
print(circle1.diameter())