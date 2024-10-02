class Rectangle():
    def __init__(self,width,height):
        self.width= width
        self.height= height

    def area(self):
        return self.width*self.height
          
    def perimeter(self):
            return 2*(self.width+self.height)
        
rect=Rectangle(5,7)
area=rect.area()
perimeter=rect.perimeter()
print(f"kenarlari {rect.width} ve {rect.height} olan dikdortgenin;"
      f" alani:{area}, cevresi:{perimeter} dir.")
