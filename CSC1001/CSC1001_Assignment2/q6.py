def check(queens):  #Function to check if the combination of queens are valid
    for queen in queens:    #Search in every queen
        for anotherQueen in queens: #Search in every other queens
            if queen==anotherQueen: #If the queens are identical, it means we get the same queen.
                continue    #Skip this
            if queen[0]==anotherQueen[0] or queen[1]==anotherQueen[1] or abs(queen[0]-anotherQueen[0])==abs(queen[1]-anotherQueen[1]):  #If the queens meet each other
                return False    #It's invalid
    return True #If every 2 queens don't meet each other, it's valid.

def printBoard(queens): #Function to print the board
    for row in range(8):    #Loop through all rows
        for column in range(8): #Loop though all column
            if (row,column) in queens:  #If there is a queen in this position
                print("|Q",end="")  #Print the block with Q
            else:   #If ther is not
                print("| ",end="")  #Print the block without Q
        print("|")  #Print the right bound

def find(): #Find the queens by Searching every possible positions
    queens=[]   #Init queens list
    for a in range(8):  #Search 1st queen
        for b in range(8):  #Search 2nd queen
            for c in range(8):  #Search 3rd queen
                for d in range(8):  #Search 4th queen
                    for e in range(8):  #Search 5th queen
                        for f in range(8):  #Search 6th queen
                            for g in range(8):  #Search 7th queen
                                for h in range(8):  #Search 8th queen
                                    queens.append((0,a))    #Add 1st queen to the list
                                    queens.append((1,b))    #Add 2nd queen to the list
                                    queens.append((2,c))    #Add 3rd queen to the list
                                    queens.append((3,d))    #Add 4th queen to the list
                                    queens.append((4,e))    #Add 5th queen to the list
                                    queens.append((5,f))    #Add 6th queen to the list
                                    queens.append((6,g))    #Add 7th queen to the list
                                    queens.append((7,h))    #Add 8th queen to the list
                                    if check(queens):   #Check if the combination is valid
                                        return queens   #Return this combination
                                    queens=[]   #Reset the list

printBoard(find())  #Call the Find() function and print the valid combination