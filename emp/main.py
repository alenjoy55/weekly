from login import*
from admin import*
from user import*
print('''
    1.login
    2.exit
''')
choice=int(input('enter the choice: '))
if choice==1:
    f,user=login()
    if f==1:
        while True:
            print('''
                1.add employee
                2.update employee
                3.delete a employee
                4.display employee
                5.logout
            ''')
            admin_choice=int(input('enter your choice: '))
            if admin_choice==1:
                add_emp()
            elif admin_choice==2:
                admin_update()
            elif admin_choice==3:
                admin_delete()
            elif admin_choice==4:
                admin_display()
            elif admin_choice==5:
                break
            else:
                print('invalid choice!!!')
    elif f==2:
        while True:
            if user['date_of_birth']==user['passw']:
                passw=input('enter a new password')
                user['password']=passw
            else:
                print('''
                    1.view profile
                    2.edit profile
                    3.logout
''')
    elif f==0:
        print('invalid user name or password!!!')