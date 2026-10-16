# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MyError(Exception):
     ...

class MyError2(Exception):
    ...

def raise_error():
    exception_note = MyError('a', 'b', 'c')
    raise exception_note

try:
    raise_error()
except (MyError, ZeroDivisionError) as e:
    print(e.__class__.__name__)
    print(f"Erro: {e.args}")
    print()
    exception_note = MyError2('ovo mandar dinovo')
    raise exception_note from e