## Herança simples

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def tell_class_name(self):
        print(self.name, self.surname, self.__class__.__name__)

class Client(Person):
    ...

class Student(Person):
    ...


c1 = Client('Manoel','Silveira')
a1 = Student('José','Otávio')

c1.tell_class_name()
a1.tell_class_name()
