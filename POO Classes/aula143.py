from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    @abstractmethod
    def name(self):...
    
class Foo(AbstractFoo):
    name = '' ### isso substitui a propriedade name da classe abstrata, mas não é o mesmo que sobrescrever o método name da classe abstrata

    def __init__(self, name):
        super().__init__(name)

    #### codigo abaixo foi substituido pelo atributo name da classe Foo, mas não é o mesmo que sobrescrever o método name da classe abstrata
    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name

foo = Foo('Bar')
print(foo.name)
