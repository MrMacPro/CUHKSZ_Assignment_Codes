from math import sin                                                #import sin function from math library
from math import cos                                                #import cos function from math library
from math import tan                                                #import tan function from math library
from MyLib import InputNum                                          #import InputNum function from MyLib
from MyLib import InputPInt                                         #import InputPInt function from MyLib

#input function
function=None                                                       #init the function string
validFunction={'sin','cos','tan'}                                   #valid function: sin cos tan
while function==None :                                              #loop until the input is a valid funtion
    function=input("Enter the function 'sin' or 'cos' or 'tan':")   #input function name
    if function not in validFunction :                              #check if the input is a valid function
        function=None                                               #if isn't, reset the input to continue the loop
        print("Please enter a valid function")                      #output error message

#input interval[a,b]
a=InputNum("Enter the left side of the interval:")                  #input a
b=InputNum("Enter the right side of the interval:")                 #input b

#input num of sub-intervals
n=InputPInt("Enter the number of sub-intervals:")

#calculate numerical integration
numericalIntegration=0                                              #init numerical integration as 0
for i in range (1,n+1) :                                            #calculate the sum
    numericalIntegration+=eval('((b-a)/n)*'+function+'(a+(((b-a)/n)*(i-1/2)))')     #add each term to sum with the formula

print(numericalIntegration)                                         #output the numerical integration