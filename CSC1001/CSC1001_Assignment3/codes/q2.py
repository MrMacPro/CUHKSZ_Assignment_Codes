class Polynomial:   #derivative calculation class
    def __init__(self,originalFunc):    #the class contains 2 data fields:
        self.func=originalFunc  #the original function

    def derivative(self):   #a method to take the derivative of original function
        for i in self.func: #Check what is the variable in the function
            if i not in "+-*^1234567890.":
                var=i
                break

        ans=''
        self.func=self.func.replace('-','+-')
        terms=self.func.split('+')    #Slice original function into terms by spliting with + symbol
        count=0
        for term in terms:
            if term.startswith('-'):    #Check if is negative
                IsMinus=True
                term=term[1:]
            else:
                IsMinus=False

            if var not in term: #This is a constant term.
                term=[]
            else:   #This is not a constant term.
                if term[0]==var:    #Handle the case coefficient is 1 and ignored
                    term='1*'+term
                
                if term[term.find(var)-1]!='*': #Handle the case if '*' is ignored
                    term=term[:term.find(var)-2]+'*'+term[term.find(var)-2:]

                newterm=[]
                newterm.append(term[:term.find(var)-1]) #Slice the coefficient into first element
                newterm.append('*')
                newterm.append(var)
                newterm.append('^')
                newterm.append(term[term.find(var)+2:]) #Slice the power into last element
                if term[term.find(var)+2:]=='': #If there is no default power
                    newterm=newterm[:-2]    #Slice off empty elements
                term=newterm


                if term[-1]==var:   #If the power is 1
                    term=term[:-2]  #Slice off 2 character "*x"
                else:
                    term[0]=str(eval(term[0])*eval(term[-1])) #New coefficient is previous coefficient multiplies previous power
                    term[-1]=str(eval(term[-1])-1)   #New power is previous power-1
                    if term[-1]=='1': #If the power is 1 after taking derivative
                        term=term[:-2]  #Slice off 2 character "^1"
            if term!=[]:    #If this term is not empty
                if IsMinus: #Add the sign
                    ans+='-'
                else:
                    ans+='+'
                for i in term:  #Add elements in term into a string to output
                    ans+=i
        if ans[0]=='+':
            ans=ans[1:]    #Slice off extra '+'
        return ans