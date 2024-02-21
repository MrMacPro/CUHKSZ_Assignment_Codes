from MyLib import InputPInt                 #import the function in MyLib.py

#input N
n=InputPInt("Enter a positive integer:")

#output table
print("m   m+1 m**(m+1)") #print title
for m in range (1,n+1) :                    #loop from 1 to n
    print(m," ",m+1," ",m**(m+1))           #output every integer and the calculation in the range