class Counter:
    def __init__(self, number):
        self.__number = number

    def __add__(self, other):
        return Counter(self.__number + other.__number)

    def __sub__(self, other):
        return Counter(self.__number - other.__number)

    def reset(self, number):
        if number >= 100 and number <= -1:
            self.__number = 0

    def __str__(self):
        return "C({})".format(self.__number)

c1 = Counter(10)
c2 = Counter(20)
c3 = c1 + c2
c4 = c1 - c2
print('c3 =', c3)
print('c4 =', c4)

    
