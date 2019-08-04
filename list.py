saveFile = open('shopping list.txt','w')
shoppinglist = []
quitshop = False
while( quitshop == False):
 print("Welcome To Shopping List!")
 print("1.add")
 print("2.sort")
 print("3.remove")
 print("4.quit")
 print("")
 opt = int( input("Please enter the option you want to proceed with "))
 if opt == 1 :
    cnt = input("do you want to add more to the shopping list?(y,n):")
    while(cnt == 'y'):
         val = input("Enter item for the list:")
         shoppinglist.append(val)
         cnt = input("do you want to add more to the shopping list?(y,n):")         

    print("Here is your shoping list:")
    for x in range(len(shoppinglist)):
          print(shoppinglist[x])
          
 elif opt == 2 :
      shoppinglist.sort()
      print("Here is your shoping list:")
      print(shoppinglist)

 elif opt == 3 :
     print("You chose option 3")
     positiontode1 = int(input("Which item would you like to delete? (enter a number)"))
     del(shoppinglist[positiontode1])
     print(shoppinglist)
     
 elif opt == 4:
     print("You quit the program")
     quitshop = True
     print(shoppinglist)
for x in range(len(shoppinglist)): 
      saveFile.write(shoppinglist[x])
saveFile.close()

