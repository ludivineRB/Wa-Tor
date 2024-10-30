class Car:
    def __init__(self, wheels) -> None:
        self.wheels = wheels

    def test(self):
        self.wheels = 5
    
    def test2(self):
        self.wheels -= 1

car1 = Car(4)
car1.test()
print(car1.wheels)
car1.test2()
print(car1.wheels)