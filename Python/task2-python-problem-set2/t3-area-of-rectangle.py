class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def Calculate_Area(self):
        return self.width * self.height

Object_r = Rectangle(10, 12)

print("Area of rectangle:", Object_r.Calculate_Area())


