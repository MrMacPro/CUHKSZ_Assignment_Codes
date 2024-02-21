from MyLib import InputNum  #import the function in MyLib.py


#input m
m=InputNum("Enter m:")

#find n with while loop
n=0                         #find from n=0
while n*n<=m :              #check if n*n>m
    n+=1                    #if not, add 1 stepping

print(n)                    #print the result