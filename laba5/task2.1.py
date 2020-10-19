class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width
class Triangle(Shape):
    def area(self):
        ar=(self.width*self.height)/2
        return ar
class Rectangle(Shape):
    def area(self):
        if self.width==self.height:
            ar = self.width * self.height
        else:
            exit() #не является квадратом



