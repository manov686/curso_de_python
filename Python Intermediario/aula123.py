# Escopo da classe e de métodos da classe
class Animal:
    # nome = 'leão'  # atributo de classe

    def __init__(self, nome):
        self.nome = nome  # atributo de instância
    def acao(self, alimento):
        return f'O {self.nome} está comendo {alimento}'
    def executar(self, *args, **kwargs):
        return self.acao(*args, **kwargs)

animal1 = Animal('tigre')

# print(Animal.nome)          # acessando atributo de classe
print(animal1.nome)           # acessando atributo de instância
# print(animal1.acao('carne'))  # acessando método da instância
print(animal1.executar('carne'))  # acessando método da instância através do método executar