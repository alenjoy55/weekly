emp=[{'id':101,'name':'alen','age':22,'salary':45000,'place':'tsr','dob':'26/10/2002','password':'26/10/2002'}]
def add_emp():
    id=int(input('enter the id: '))
    f=0
    for i in emp:
        if i['id']==id:
            f=1
            print('existing id...')
            add_emp()
    if f==0:
        name=input('enter the name: ')
        age=int(input('enter the age: '))
        salary=int(input('enter the salary: '))
        place=input('enter the place: ')
        dob=input('enter the dob: ')
        user_pass=dob
        emp.append({'id':id,'name':name,'age':age,'salary':salary,'place':place,'dob':dob,'password':user_pass})
        print('employee added successfully....')
        print(emp)
        
