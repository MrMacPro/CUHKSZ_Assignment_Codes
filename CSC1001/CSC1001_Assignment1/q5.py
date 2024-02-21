from MyLib import InputPInt                             #import the function in MyLib.py

#input N
n=InputPInt("Enter a positive integer:")

#print the text output
print("The prime numbers smaller than",n,"include:")

primeCount=0                                            #count the number of prime
#search every integer smaller than N
for num in range (2,n):
    #check if num is a prime number
    numIsPrime=True
    for i in range (2,num+1):                           #search every integer1 <= num
        for j in range (2,num+1):                       #search every integer2 <= num
            if i*j==num :                               #if num can be expressed as product of 2 integer,
                numIsPrime=False                        #it isn't a prime number.
    if numIsPrime :                                     #if num can't be expressed as product of 2 integer,
        print(num,end=" ")                              #print multiple prime number
        primeCount+=1                                   #count the prime number
    if primeCount==8 :                                  #output 8 prime number in a row
        print()                                         #when there are already 8 number in a row, enter a new line
        primeCount=0                                    #reset the counter of prime number for next row