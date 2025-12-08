# BEGIN (write your solution here)
class RegistrationError(Exception):
    def __init__(self):
        self.name = 'RegistrationError'
        self.message = 'Ошибка регистрации'

class InvalidEmailError(RegistrationError):
    def __init__(self):
        super().__init__()
        self.name = 'InvalidEmailError'
        self.message = 'Некорректный email'

class PasswordsNotMatchError(RegistrationError):
    def __init__(self):
        super().__init__()
        self.name = 'PasswordsNotMatchError'
        self.message = 'Пароли не совпадают'

class UserExistsError(RegistrationError):
    def __init__(self):
        super().__init__()
        self.name = 'UserExistsError'
        self.message = 'Пользователь с таким email уже существует'
# END
