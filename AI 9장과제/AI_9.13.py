class Rectangular:
    
    
    def __init__(self, x, y, width, heigth):
        
        self.__x = x
        self.__y = y
        self.__width = width
        self.__heigth = heigth

    def set_x(self, x):
        self.__x = x
   
        
            

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y

    def set_width(self, width):
        if width > 0:
            self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, heigth):
        if heigth > 0:
            self.__heigth = heigth

    def get_heigth(self):
        return self.__heigth

    def area(self, width, heigth):
        
        return self.__width * self.__heigth

    def contain(self, other):
        if self.__x == other.__x and self.__width < other.__width:
            return self.__x.__eq__(other.__x) and self.__width.__lt__(other.__width)

    def overlap(self, other):
        if self.__y == other.__y and self.__heigth == other.__heigth:
            return self.__y.__eq__(other.__y) and self.__heigth.__eq__(other.__heigth)
        
    def __str__(self):
        return 'Rectangular : (x='+str(self.__x)+', y='+str(self.__y)+', w='+str(self.__width)+', h='+str(self.__heigth)+', 면적:'+str(self.__width * self.__heigth)+')'

r1 = Rectangular(0, 0, 100, 100)
r2 = Rectangular(0, -10, 10, 10)
r3 = Rectangular(-100, 0, 120, 100)

print('r1 =', r1)
print('r2 =', r2)
print('r3 =', r3)

print('r1 contain r2 :', r1.contain(r2))
print('r1 contain r3 :', r1.contain(r3))
print('r1 overlap r2 :', r1.overlap(r2))
print('r1 overlap r3 :', r1.overlap(r3))

