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
            f'{self.brand.name} '
            f'{self.name}, '
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
motor2 = Motor('1.0', 100)
motor3 = Motor('2.0', 190)

ford = Manufacturer('Ford')
chevrolet = Manufacturer('GM Chevrolet')
fiat = Manufacturer('Fiat')

mustang = Car('Mustang')
mustang.brand = ford
mustang.motor = motor1

onix = Car('Onix')
onix.brand = chevrolet
onix.motor = motor2

focus = Car('Focus')
focus.brand = ford
focus.motor = motor3

uno = Car('Uno')
uno.brand = fiat
uno.motor = motor2

mustang.list_car()
onix.list_car()
focus.list_car()
uno.list_car()