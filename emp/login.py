def login():
    uname=input('enter your username: ')
    passw=input('enter your password: ')
    f=0
    if uname=='admin' and passw=='admin':
        f=1
        return f