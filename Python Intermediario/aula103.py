#Funções decoradoras

def create_func(func):
    def intern(*args, **kwargs):
        for arg in args:
            isstring(arg)

        result = func(*args, **kwargs)
        return result

    return intern


def invert_str(string):
    return string[::-1]


def isstring(param):
    if not isinstance(param, str):
        raise TypeError('param needs to be a string')


check_param = create_func(invert_str)

invert = check_param('Python')
print(invert)