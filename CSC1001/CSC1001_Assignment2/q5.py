def printState(lst):    #Function to print the state of lockers
    print("Open lockers include:",end=' ')  #Header
    for i in range(len(lst)):   #Search every element in target list
        if lst[i]:  #If it is True
            print(i+1,end=' ')  #Print the number

    print("\nClosed lockers include:",end=' ')  #Header
    for i in range(len(lst)):   #Search every element in target list
        if not lst[i]:  #If it is True
            print(i+1,end=' ')  #Print the number

lockers=[]  #Init the lockers list
for num in range(100):  #Init list into False which means closed
    lockers.append(False)

for student in range(1,101):    #Search every students
    for locker in range(1,101): #Search every lockers
        if locker%student==0:   #If the locker fulfill certain scenario
            lockers[locker-1]=not lockers[locker-1] #Change the state of locker

printState(lockers) #Print the open and closed locker