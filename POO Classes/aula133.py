# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

#### CÓDIGO DO TEACHER:####
from functools import partial

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__exemplo = 'isso é private'

    def metodo_publico(self):
        # self._metodo_protected()
        # print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'

f = Foo()
# print(f.public)
# print(f.metodo_publico())
# print(f.__metodo_private())  # AttributeError: 'Foo' object has no attribute '__metodo_private'
print(f._Foo__metodo_private())  # isso funciona, mas não é recomendado


#### MEU CÓDIGO:####

# class Foo:
#     def __init__(self):
#         self.public = 'isso é público'
#         self._protected = 'isso é protegido'
#         self.__private = 'isso é privado'

#         self._method_protected()

#     def public_method(self):
#         # return 'isso é um método público'
#         print(self.__private)
#         return '__private'
    
#     def _method_protected(self):
#         print('isso é um método protegido')
#         return 'isso é protegido'
        
#     def __method_private(self):
#         print('priv method')
#         return 'private method'


# f = Foo()
# print(f._Foo__method_private())
# print(f.public_method())
# # print(f.public)
# # print(f.public_method())