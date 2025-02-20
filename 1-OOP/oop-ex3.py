### Exercise 3 Abstract Method
from abc import ABC, abstractmethod
import math

class Shape(ABC):
  def __init__(self, color):
    # Initialize color property
    self.color = color

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Rectangle(Shape):
  def __init__(self, color, length, width):
    self.color = color
    self.length = length
    self.width = width

  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return 2*(self.length + self.width)

class Circle(Shape):
  def __init__(self, color, radius):
    self.color = color
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2

  def perimeter(self):
    return 2 * math.pi * self.radius

# Test your implementation
rectangle1 = Rectangle("red", 4, 5)
print(rectangle1.area())  # Should output 20
print(rectangle1.perimeter())  # Should output 18

circle1 = Circle("blue", 3)
print(circle1.area())  # Should output approximately 28.274333882308138
print(circle1.perimeter())  # Should output approximately 18.84955592153876