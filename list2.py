saveFile = open('shopping list.txt','w')
def addlist(shoppinglist):
    val = input("Enter item for the list:")
    shoppinglist.append(val)
    for x in range(len(shoppinglist)):
        print(shoppinglist[x])
def sortlist(shoppinglist):
    shoppinglist.sort()
    print("Here is your shoping list:")
    print(shoppinglist)
def removelist(shoppinglist):
    positiontode1 = int(input("Which item would you like to delete? (enter a number)"))
    del(shoppinglist[positiontode1])
def quitlist(shoppinglist):
    print("You quit the program")


shoppinglist = []
quitshop = 'n'
print("Welcome To Shopping List!")
print("1.add")
print("2.sort")
print("3.remove")
print("4.quit")
print("")
while( quitshop == 'n'):
    cnt ='y'
    opt = int( input("Please enter the option you want to proceed with "))
    if opt == 1 :
        while(cnt == 'y'): 
           addlist(shoppinglist)
           cnt = input("do you want to add more to the shopping list?(y,n):")
    elif opt == 2 :
        sortlist(shoppinglist)
    elif opt == 3 :
        removelist(shoppinglist)
    elif opt == 4 :
        quitlist(shoppinglist)
        
    quitshop = input("do you want to quit the shop?")
for x in range(len(shoppinglist)): 
      saveFile.write(shoppinglist[x])
saveFile.close()    
