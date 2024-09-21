print("****tv shedule****")
import datetime
tv=[]
while True:
    print('''
        1.add item
        2.view item
        3.update
        4.delete
        5.search
        6.exit
    ''')
    choice=int(input('choose an option: '))
    if choice==1:
        chl=int(input("enter channel: "))
        day=input("enter a day: ")
        prg_name=input("prg_name: ")
        time=(input("enter time: "))
        tv.append([chl,day,prg_name,time])
    elif choice==2:
        if tv:
         print('{:<10}{:<10}{:<10}{:<5}'.format("chl","day","prg_name","time"))
         for i in tv:
            print('{:<10}{:<10}{:<10}{:<5}'.format(i[0],i[1],i[2],i[3]))
    elif choice==3:
        chl=int(input("enter a channel: "))
        for i in tv:
            if i[0]==chl:
                print("1.update day")
                print("2.update program")
                print("3.update time")
                update_choice=int(input("enter choices"))
                if update_choice==1:
                    i[1]=input("enter new day: ")
                elif update_choice==2:
                    i[2]=input("enter the new program: ")
                elif update_choice==3:
                    i[3]=int(input("enter new time: "))
                    print("program details update succesfully!")
                    break
                else:
                    print("not found.")
    elif choice == 4:
        ch1 = int(input("Enter channel number to remove: "))
        for i in tv:
            if i[0] == ch1:
                tv.remove(i)
                print("Channel removed successfully!")
                break
        else:
            print("Channel not found.")

    elif choice == 5:
        ch1=int(input("Enter channel Number to search: "))
        for i in tv:
            if i[0] == ch1:
                print('_' * 70)
                print('{:<10}{:<20}{:<15}{:<15}'.format('chl', 'day', 'prg_name', 'time'))
                print('_' * 70)
                print('{:<10}{:<20}{:<15}{:<15}'.format(i[0], i[1], i[2],i[3]))
                break
        else:
            print("Channel not found.")

    elif choice==6:
        print("unavailable channel!")
        break

    else:
        print("Invalid Choice.")
           