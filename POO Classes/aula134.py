# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__ (self, nome) -> None:
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrita:
    def __init__ (self, nome) -> None:
        self.nome = nome    

    # def escrever(self):
    #     return f'{self.nome} está sendo usada para escrever'
        
    def escrever(self, escritor):
        return f'{escritor.nome} está usando {self.nome} para escrever'

escritor1 = Escritor("Manoel")
ferramenta1 = FerramentaDeEscrita("caneta preta")
escritor1.ferramenta = ferramenta1

escritor2 = Escritor("Victor")
ferramenta2 = FerramentaDeEscrita("lápis")
escritor2.ferramenta = ferramenta2 

# print(ferramenta.escrever()) 
print(escritor1.ferramenta.escrever(escritor1))
print(escritor2.ferramenta.escrever(escritor2))