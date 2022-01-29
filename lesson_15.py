from typing import List,Set,Tuple, Union

def check_password(key: Union[List, Tuple, Set, str],)-> Union[int, List, Tuple, str]:
   '''
   The function checks for the presence of a login in the global dictionary
   :param key: login
   :return: true or false
   '''''
    def wrapper():
   # return temp.get(key)
    return any(key for key in temp.keys())
return wrapper

def authenticate(a):
'''
User authentication function
:return: any Return of truth
'''
    def wrapper():
    if   check_password()==True:
        return f'Вы в систепме!'
    else:
        for i in range(3):
            if check_password()!=True:
            n=3-i
            return f'Не правильное Имя или Пароль. У вас осталось {n} попыток'
        if n==3:
            return f'Попытки истекли'
return wrapper

@authenticate
@check_password
def login(username,password):
    return True

if _name_=='_main_':
    temp={}
    username=input()
    password=input()
    print(login(username,password))

