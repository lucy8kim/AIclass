class Car:
    speed = 0

    def upSpeed(self, value):
        self.speed = self.speed + value



class RVCar(Car): #Car 클래스를 RVCar 클래스에 상속
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum

