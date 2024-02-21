from MyLib import InputNum                                      #import the function in MyLib.py

#input value
finalAccountValue=InputNum("Enter the final account value:")    #input final account value
annualInterestRate=InputNum("Enter the annual interest rate:")  #input annual interest rate (this should input in percent)
numberOfYears=InputNum("Enter the number of years:")           #input number of years

#calculate and output initialDepositAmount
initialDepositAmount=finalAccountValue/((1+0.01*annualInterestRate)**numberOfYears)
print("The initial value is:",initialDepositAmount)             #print the initial deposit amount