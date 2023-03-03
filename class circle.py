#program to calculate the area of a circle
class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    a = 3.142 * self.radius**2
    return a
    
  def perimeter(self):
    p = 3.142 * self.radius * 2
    return p

c = Circle(10)
print(c.area())
print(c.perimeter())
