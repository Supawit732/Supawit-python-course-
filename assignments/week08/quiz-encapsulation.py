"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""
class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
        
    def getArea(self):
        Area = self.__width * self.__length
        return f"Area = {Area}"
    
    def getPerimeter(self):
        Perimeter = 2 * (self.__width + self.__length)
        return f"Perimeter = {Perimeter}"
    
    def  isSquare(self):
        return self.__length == self.__width
rect = Rectangle(5,5)
print(rect.getArea())
print(rect.getPerimeter())
print(rect.isSquare())
print( )
rect = Rectangle(6,8)
print(rect.getArea())
print(rect.getPerimeter())
print(rect.isSquare())
    