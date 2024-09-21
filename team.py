print("**********football management system**********")
football = []

while True:
    print("""
    1. Add player
    2. view player Details
    3. player updates
    4. search player
    5. delete player
    6. view available player
    7.exit
    """)
    
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        id=int(input("Enter player ID : "))
        pl_name = input("Enter a Name: ")
        pl_nation = input("enter player nation: ")
        pl_position = input("Enter position: ")
        pl_jersy=int(input("Enter a jersy number: "))
        pl_stats=input("player available or unavailable: ")
        football.append({'id':id,'name': pl_name,'nation':pl_nation,'position':pl_position,'pl_jersy':pl_jersy,'pl_stats':pl_stats})
        print("Player added successfully!")
        
    elif choice == 2:
        print('_' * 90)
        print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('id', 'Name','nation', 'Position', 'jersy','stats'))
        print('*' * 90)
        for i in football:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['id'], i['name'],i['nation'],i['position'], i['pl_jersy'],i['pl_stats']))
        # else:
        #      print("player not found!")
    
    elif choice== 3:
         pl_id=input("enter the id of player to update: ")
         for i in football:
              if i['id']==id:
                   pl_position=input("enter a new position: ")
                   pl_jersy=int(input("enter a new jersy number: "))
                   i['position']=pl_position
                   i['pl_jersy']=pl_jersy
                   print("player updated successfully")
                   break
         else:
              print("player id not in database.")
    elif choice==4:
        pl_id = input("Enter the player id to Search: ")
        for i in football:
            if i['id'] == id:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('id','name', 'nation', 'position','jersy','stats'))
                print('{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(i['id'],i['name'], i['nation'], i['position'],i['pl_jersy'],i['pl_stats']))
                break
        else:
            print("***Player not found***")            
    elif choice==5:
         id=int(input("enter the id to be delete: "))
         f=0
         for i in football:
              if i['id']==id:
                   football.remove(i)
                   f=1
                   print("removed successfully! ")
         if f==0:
              print("invalid id!!!")
    elif choice==6:
         print('_'*90)
         print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format('id','name','nation','position','jersy','stats'))
         print('_'*90)
         for i in football:
              if i['pl_stats']=='available':
                   print("{:<10}{:<15}{:<15}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['nation'],i['position'],i['pl_jersy'],i['pl_stats']))
    elif choice==7:
         break
    else:
         print("invalid!!")

     #     ch_id=int(input("enter coach id: "))
     #     ch_name=input("enter coach name: ")
     #     ch_nation=input("coach nation: ")
     #     tatics=input("enter coach tatics: ")
     #     contract=int(input("enter contract: "))
     #     football.append({'coach_id':ch_id,'coach_name':ch_name,'nation':ch_nation,'tatics':tatics,'contract':contract})
     #     print("coach added successfully! ")

         


              

