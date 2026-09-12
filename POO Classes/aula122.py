# Entendendo self em classes Python
# Classe - Molde
# Instância - Objeto
# Uma classe é um molde para criar objetos, e cada objeto é uma instância da classe.
# O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis que pertencem à classe.

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

car1.acelerate()
Car.acelerate(car1) # same thing 

# Car.acelerate(car2)
# Car.acelerate(car3)