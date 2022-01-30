
def check_password(func: object) -> object:
    """

    :type func: object
    """
    def wrapper(username, password):
        return any(key for key, value in temp.items() if key==username and value==password)

    return wrapper


@check_password
def orig(username, password):
 return True

if __name__ == '__main__':
    temp = {'yara': '13444!', 'dav': '2345v'}

    print(orig('yaa', '13444!'))