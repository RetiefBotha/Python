
name = input("Who is comming to the part? ")
list = []
ind = 0
Counter = 0
#Append Function
while (name != "none"):
   
    list.append(name)
    name = input("Who else is comming? ")
    Counter += 1


print(list)

#Insert Function
for i in range(Counter):
    womName = str(list[ind])
    husName = input("Who is the husband of "+womName+" ? ")
    list.insert(ind+1,husName)
    ind += 2
else:
    print(list)

#Delete Function    
delName = input("Do you want to delete a name from the list? ")
if (delName == "yes"):
    delete = input("Who do you want to remove? ")
    list.remove(delete)
    print(list)
else:
    #Reverse Function
    list.reverse()
    print(list)
    
    print("Your are happy with the list, get ready to party!!!")


