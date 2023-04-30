# Создать статический метод который принимает на вход три параметра: login, password и confirmPassword.
# Login должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина login должна быть меньше 20 символов. Если login не соответствует этим требованиям, 
# необходимо выбросить WrongLoginException.
# Password должен содержать только латинские буквы, цифры и знак подчеркивания.
# Длина password должна быть меньше 20 символов. Также password и confirmPassword должны быть равны. 
# Если password не соответствует этим требованиям, необходимо выбросить WrongPasswordException.
# WrongPasswordException и WrongLoginException - пользовательские классы исключения 
# с двумя конструкторами – один по умолчанию, второй принимает сообщение исключения 
# и передает его в конструктор класса Exception.
# Обработка исключений проводится внутри метода.
# Используем multi-catch block.
# Метод возвращает true, если значения верны или false в другом случае.
import re

class WrongLoginException(Exception):
    def __init__(self, message=""):
        super().__init__(message)

class WrongPasswordException(Exception):
    def __init__(self, message=""):
        super().__init__(message)

def validate_login_and_password(login, password, confirm_password):
    login_regex = "^[a-zA-Z0-9_]{1,20}$"
    password_regex = "^[a-zA-Z0-9_]{1,20}$"
    
    try:
        if not re.match(login_regex, login):
            raise WrongLoginException("Login должен содержать только латинские буквы, цифры и знак подчеркивания. Длина login должна быть меньше 20 символов.")
        
        if not re.match(password_regex, password):
            raise WrongPasswordException("Password должен содержать только латинские буквы, цифры и знак подчеркивания. Длина password должна быть меньше 20 символов.")
        
        if password != confirm_password:
            raise WrongPasswordException("Password и confirmPassword должны быть равны.")
        
        return True
    
    except (WrongLoginException, WrongPasswordException) as e:
        print(e)
        return False
    
if __name__=='__main__':
    validate_login_and_password(input('login:'),input('password:'),input('confirm_password:'))