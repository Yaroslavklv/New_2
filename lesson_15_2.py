
def tag_p(func: object) -> object:
    def wrapper(*args,**kwargs):
        before='<p>'
        after='</p>'
        print(args,kwargs)
        rezult=func(*args,**kwargs)

        return f'{before}{rezult}{after}'

    return wrapper

@tag_p
def orig(username, password):
    return username, password

if __name__ == '__main__':
    orig('david', '123fd')