class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'Dog(이름은 '+self.name+'이고, 나이는 '+str(self.age)+'살입니다.)'



my_dog = Dog('Mango', 3)
print(my_dog)
