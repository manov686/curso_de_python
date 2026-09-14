# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user): #setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in password):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in password):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(char.islower() for char in password):
            raise ValueError('Password must contain at least one lowercase letter')
        return True
    
    @staticmethod
    def log(message):
        print(f'LOG: {message}')

c1 = Connection.create_with_auth('root', 'S1spta251')
# c1 = Connection()
# c1.set_user('root')
# c1.set_password('S1spta251')
print(Connection.log('Vai dar mensagem de None abaixo XD'))
print(f'User: {c1.user}')
print(f'Password: {c1.password}')