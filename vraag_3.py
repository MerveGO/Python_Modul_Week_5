class Shape:
    def __init__(self,width,height):
        self.width= width
        self.height= height
   
class Rectangle(Shape):
    def calculate_area(self):
        return  self.width*self.height

class Square(Shape):
    def calculate_area(self):
        return  self.width*self.width
    
rect=Rectangle(5,10)
area_rect=rect.calculate_area()

square=Square(4,4)
area_square=square.calculate_area()

print(f"Dikdortgenin alani={area_rect}")
print(f"Kareninin alani={area_square}")