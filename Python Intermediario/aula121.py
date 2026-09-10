# Métodos em instâncias de classes Python

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def description(self):
        return f'{self.brand} {self.model}'
    def acelerate(self):
        return f'{self.model} is acelerating!'

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Volkwagen", "Beetle")

# print(car1.description())
# print(car2.description())
# print(car3.description())
# print()
# print(f'Carro 1:  {car1.model}')
# print(f'Carro 2:  {car2.model}')
# print(f'Carro 3:  {car3.model}')

print(car1.acelerate())
print(car2.acelerate())
print(car3.acelerate())
