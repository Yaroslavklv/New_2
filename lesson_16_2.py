from typing import List,Set,Tuple, Union

TEMP = {'y':'1', 'yara':'143!'}

def decorate(func: any)->bool:
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
    return any(key for key, value in TEMP.items() if key==username and value==password)


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

 import argparse
 prov_parser = argparse.ArgumentParser()
 prov_parser.add_argument("-u", "--username", action="store")
 prov_parser.add_argument("-p", "--password", action="store")
 args = prov_parser.parse_args()
 print(args)
 if (args.username == None) and (args.password == None):
     print("Введите значение username и password")
 elif args.username == None:
     print("Введите значение username")
 elif args.password == None:
     print("Введите значение password")
 count = 3
 while count != 0:
     per = login(args.username, args.password)
     if per == True:
         print(f'Вы в системе!')
         break
     else:
         count -= 1
         print('Неверный пароль. У вас осталось ', count, 'попыток')
         args.username=input()
         args.password=input()
         print(args)
 else:
     print(f'Попытки истекли')