def isPrime(num):   #Define a function to check if input is a prime number
    flag=True   #Init a flag var to identify set a status of whether num is prime
    for divisor in range (2,num): #Loop in every int<num
        if num%divisor==0:    #If num is divisible by any of int<num
            flag=False  #Set prime status into False
    return flag #Return the result

def printList(lst): #Define a function to print the result in format of 10/row
    numInRow=0  #Count the position of current element
    for element in lst:   #Loop in the list to output all element
        numInRow+=1 #Add 1 to count

        #Modified afterward(points deducted for this block below)
        #The digits should be right aligned
        if element<100:
            print(" ",end="")
        if element<1000:
            print(" ",end="")

        print(element,end=" ")    #Output the element without creating newline
        if numInRow==10:    #If the number in a row reaches 10
            numInRow=0  #Reset the counter
            print() #Create a newline

count=0 #Init count var
num=12  #Init the num to check if it is an emirp. The first emirp is 13 so it can be any int<=12
lst=[]  #Init the list to store the output
while True: #Loop until we find 100 emirps
    num+=1  #Find next num to check
    reverseNum=int(str(num)[::-1])  #Reverse the target num
    if num==reverseNum: #If the num is palindromic
        continue    #Skip this number
    if isPrime(num) and isPrime(reverseNum):    #Call isPrime() function for num and reversed num to check if this num is emirp
        lst.append(num) #If it is emirp, add it to the output list.
        count+=1    #Add 1 to count
        if count==100:  #If count reaches 100
            break   #We're done finding and exit this loop

printList(lst)  #Call printList() function to print the output list with certain format