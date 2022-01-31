from typing import List,Set,Tuple, Union

def decorate (func: any)->bool:
    """
    Decorator function. Checks for data transfer between functions the check_password and authenticate
    :param func:
    :return: Takes the value of a function parameter
    """
    def wrapper(username:any, password:any)->bool:
        if not check_password(username, password):
            return False
        if not authenticate(username, password):
            return False
        return func(username, password)

    return wrapper

def check_password(username:str, password:str)->bool:
    """
    The function checks for the presence of a login in the global dictionary
    :param username:
    :param password:
    :return: true or false
    """
    return any(key for key, value in temp.items() if key==username and value==password)

def authenticate(username:any, password:any)->bool:
    """
    The function authenticates the user
    :param username:
    :param password:
    :return: brings out the truth
    """
    return True

@decorate
def login(username:any, password:any)->bool:
    """
    The function enters into something
    :param username:
    :param password:
    :return: brings out the truth
    """
    return True

if __name__ == '__main__':
    temp = {}
    count = 3
    while count != 0:
        per=login(username=input(), password=input())
        if per == True:
            print(f'Вы в системе!')
            break
        else:
            count -= 1
            print('Неверный пароль. У вас осталось ', count, 'попыток')
    else:
        print(f'Попытки истекли')
