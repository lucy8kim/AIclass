class Car:
    def method(self):
        print("슈퍼 클래스")


class Sedan(Car):
    def method(self):
        print("서브 클래스")



myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method()

#정답: 3(슈퍼 클래스 서브 클래스)
#풀이
#[1] = myCar.method() 는 Car()가 인스턴스, Car 클래스   >> print("슈퍼 클래스")실행
#[2] = mySedan.method() 는 Sedan()이 인스턴스, Sedan 클래스  >> print("서브 클래스")실행

    
