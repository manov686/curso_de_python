# Métodos em instâncias de classes Python

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return f'{self.brand} {self.model}'
    def acelerate(self):
        print(f'{self.model} is acelerating!')

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Volkwagen", "Beetle")

Car.acelerate(car1)
Car.acelerate(car2)
Car.acelerate(car3)