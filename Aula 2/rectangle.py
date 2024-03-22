import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height




    def calculatePerimeter():
        return (self.height + self.width)*2

    def calculateArea():
        return (self.height * self.width)
    




class Test(unittest.TestCase):
    

    def test_perimeter(self):
        rectangle = Rectangle(5, 10)
        target = 30
        self.assertEqual(rectangle.calculatePerimeter(), target)

    def test_area(self):
        rectangle = Rectangle(5, 10)
        target = 50
        self.assertEqual(rectangle.calculateArea(), target)



    