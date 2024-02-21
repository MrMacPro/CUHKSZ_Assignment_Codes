def isValid(number):    #Function check if card num is valid
    try:    #Use try & except expression to check if it is number
        eval(number)    #Use eval() to generate error whhen it isn't a number
    except:
        return False    #Input is not valid if it's not a number
    
    if int(number)!=eval(number):   #Check if this num is an int
        return False    #Input is not valid if it's not an int

    validLength=range(13,17) #Only 13 digits to 16 digits are valid number
    if len(str(number)) not in validLength: #If the length is valid
        return False    #Input is not valid if it's length is invalid
    
    
    validStart={'4','5','6','37'}   #The number should start with these letters
    startValid=False    #Init the flag of valid start
    for start in validStart:    #Search every valid start
        if str(number).startswith(start):   #Check if the start is the same
            startValid=True #The start is valid as long as one of them is true
    if startValid==False:   #Start is confirmed invalid
        return False    #Input is not valid if it's start is invalid
    
    return (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10==0   #Add the sum of double even place and sum of odd place. If the result is divisible by 10, the number is valid.

def sumOfDoubleEvenPlace(number):   #Function to get the sum of double even place of a number
    sum=0   #Init the sum
    for digit in range(len(str(number))):   #Search in every digit in the number
        if digit%2==0:  #Pick out the even place
            sum+=getDigit(int(str(number)[digit])*2)    #Call getDigit() function and add the result onto the sum
    return sum  #Return the sum
    
def getDigit(number):   #Function to output number itself if there's 1 digit and the sum of each digit if there's 2 digits
    if number>9:    #If there's 2 digits
        return number%10+number//10 #Return sum of 2 digits
    else:   #If there's 1 digit
        return number   #Return itself

def sumOfOddPlace(number):  #Function to get the sum of odd place
    sum=0   #Init the sum
    for digit in range(len(str(number))):   #Search in every digit in the number
        if digit%2==1:  #Pick out the odd place
            sum+=int(str(number)[digit])    #Add the digit onto the sum
    return sum  #Return the sum

cardNumber=input("Enter a credit card number: ")    #Input the card number
print(isValid(cardNumber))  #Output if the number is valid