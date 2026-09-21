## Exercicio aula  137

class Car:
    def __init__(self, name, brand, motor):
        self.name = name
        self.brand = brand
        self.motor = motor

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

    def list_motor(self):
        print(f'Motor: {self.name}, Power: {self.power}')


class Manufacturer:
    def __init__(self, name):
        self.name = name

    def list_manufacturer(self):
        print(f'Manufacturer: {self.name}')


motor1 = Motor('V8', 500)
manufacturer1 = Manufacturer('Ford')
car1 = Car('Mustang', manufacturer1, motor1)

motor2 = Motor('3 Cilinders', 100)
manufacturer2 = Manufacturer('GM Chevrolet')
car2 = Car('Onix', manufacturer2, motor2)


car1.list_car()
car2.list_car()