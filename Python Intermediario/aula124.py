# Mantendo estados dentro da classe
class Camera:
    def __init__(self, modelo, filmando = False):
        self.modelo = modelo
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'A câmera {self.modelo} já está filmando')
            return
        print(f'A câmera {self.modelo} está filmando')
        self.filmando = True

    def parar(self):
            if self.filmando:
                print(f'A câmera {self.modelo} deixou de filmar')
                self.filmando = False
                return
            print(f'A câmera {self.modelo} não está filmando')

    def fotografar(self):
        if self.filmando:
            print(f'A câmera {self.modelo} não pode fotografar enquanto filma')
            return
        print(f'A câmera {self.modelo} está fotografando')

c1 = Camera('Canon')
c2 = Camera('Sony')

# c1.filmar()
# c2.filmar()

print(c1.filmando)
print(c2.filmando)
c1.parar()
