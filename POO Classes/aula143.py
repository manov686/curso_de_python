from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = name
        self._name = None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('sou inutil')

foo = Foo('Bar')
print(foo.name)


# class Log(ABC):
#     @abstractmethod
#     def _log(self, msg): ...

#     def log_error(self, msg):
#         return self._log(f'Error: {msg}')

#     def log_success(self, msg):
#         return self._log(f'Success: {msg}')

# class LogPrintMixin(Log):
#     def _log(self, msg):
#         print(f'{msg} ({self.__class__.__name__})')

# l = LogPrintMixin() 
# l.log_error('Hi')