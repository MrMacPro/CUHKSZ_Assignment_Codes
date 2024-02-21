#input int or float value with try and except expression and do eval
#param:text to output when getting input
def InputNum(expression):                           #defining the function
    output=None                                     #set a initial value of output
    while output==None :                            #keep looping until valid input
        try:                                        #use try and except to find a valid input
            output=eval(input(expression))          #use eval() to generate error when input is not a number
        except:                                     #
            print("Please input a valid number")    #print error message when the input is invalid
    return output                                   #return the final output

#similarly, input a positive int
def InputPInt(expression):                          #defining the function
    output=None                                     #set a initial value of output
    while output==None :                            #keep looping until valid input
        try:                                        #use try and except to find a valid input
            output=input(expression)                #get the input
            eval(output)                            #use eval() to generate error when input is not a number
        except:                                     #
            print("Please input a number")          #print error message when the input is invalid
            output=None                             #reset output value to None to continue the loop
            continue                                #skip following checks
        #check if the input value is an int
        if eval(output)%1!=0 :
            print("Please input an integer")        #print error message when the input is invalid
            output=None                             #reset output value to None to continue the loop
            continue                                #skip following checks
        #check if the input value is positive
        if eval(output)<0 :
            print("Please input a positive number") #print error message when the input is invalid
            output=None                             #reset output value to None to continue the loop
    return eval(output)                             #return the final output