
def check_password(func: object) -> object:
    """
    The function checks for the presence of a login in the global dictionary
    :type func: object
    :return: true or false
    """
    def wrapper(username, password):
        return any(key for key, value in temp.items() if key==username and value==password)

    return wrapper

def authenticate(func_2):
    """
    User authentication function
    :param func_2:
    :return:
    """

    def wrapper(username, password):
        if any(key for key, value in temp.items() if key==username and value==password) == True:
            return f'Вы в системе!'
        else:
            n=1
            while n<3:
                n += 1
                return f'Не правильное Имя или Пароль. У вас осталось {n} попыток'
            else:
                return f'Попытки истекли'

    return wrapper


@authenticate
@check_password
def orig(username, password):
 return True

if __name__ == '__main__':
    temp = {'yara': '13444!', 'dav': '2345v'}

    print(orig('y', '13444!'))