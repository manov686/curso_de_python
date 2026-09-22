## Exercicio aula  137

class Car:
    def __init__(self, name):
        self.name = name
        self._motor = None
        self._brand = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    def list_car(self):
        print(
            f'Car: {self.name}, '
            f'Brand: {self.brand.name}, '
            f'Motor: {self.motor.name}, '
            f'Power: {self.motor.power}'
        )

class Motor:
    def __init__(self, name, power):
        self.name = name
        self.power = power

class Manufacturer:
    def __init__(self, name):
        self.name = name


motor1 = Motor('V8', 500)
motor2 = Motor('3 Cilinders', 100)

manufacturer1 = Manufacturer('Ford')
manufacturer2 = Manufacturer('GM Chevrolet')

car1 = Car('Mustang')
car1.brand = manufacturer1
car1.motor = motor1

car2 = Car('Onix')
car2.brand = manufacturer2
car2.motor = motor2

car1.list_car()
car2.list_car()