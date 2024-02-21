#input an int
integer=None                                    #set a initial value of output
while integer==None :                           #keep looping until valid input
    try:                                        #use try and except to find a valid input
        integer=input("Enter an interger:")     #get the input
        eval(integer)                           #use eval() to generate error when input is not a number
    except:                                     #
        print("Please input a number")          #print error message when the input is invalid
        integer=None                            #reset output value to None to continue the loop
        continue                                #skip following checks
    #check if the input value is an int
    if eval(integer)%1!=0 :
        print("Please input an integer")        #print error message when the input is invalid
        integer=None                            #reset output value to None to continue the loop

#print each number in the integer (which is a string)
for i in integer :
    print(i)                                    #print the ith digit in the integer

#We can also accomplish the same task by continously dividing an integer by 10 and take the decimal as last digit.