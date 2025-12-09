class Circle:
    PI = 3.14
    def __init__(self, r):
        self.radius = r
    def area(self):
        return Circle.PI * self.radius * self.radius
c1 = Circle(10)
print("Area of circle 1:", c1.area())
c2 = Circle(5)
print("Area of circle 2:", c2.area())