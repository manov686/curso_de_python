def fabrica_decoradores(a=None, b=None, c=None):

    def decoradora(func):

        def aninhada(*args, **kwargs):
            print(f'Decorador: {a=}, {b=}, {c=}')
            return func(*args, **kwargs)

        return aninhada

    return decoradora


@fabrica_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


@fabrica_decoradores()
def multiplica(x, y):
    return x * y


print(soma(10, 5))
print(multiplica(10, 5))