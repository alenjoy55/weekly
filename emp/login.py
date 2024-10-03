from admin import*
def login():
    uname=input('enter your username: ')
    passw=input('enter your password: ')
    f=0
    user=''
    if uname=='admin' and passw=='admin':
        f=1
    for i in emp:
        if i['id']==uname and i['passw']==passw:
            f=2
            user=i
    return f,user