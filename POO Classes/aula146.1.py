# Notas das exceptions em Python (add_notes, __notes__)
# https://docs.python.org/3/library/exceptions.html
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções

class MyError(Exception):
     ...

class MyError2(Exception):
    ...

def raise_error():
    exception_note = MyError('a', 'b', 'c')
    raise exception_note

def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('você errou isso')
    raise exception_

try:
    levantar()
except (MyError, ZeroDivisionError) as error:
    print(error.args)
    print()
    exception_ = MyError2('Vou lançar de novo')
    exception_.__notes__ = error.__notes__.copy()
    exception_.add_note('Mais uma nota')
    raise exception_ from error