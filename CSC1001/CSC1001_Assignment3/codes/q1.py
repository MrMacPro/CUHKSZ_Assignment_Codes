class Flower:   #Flower class
    def __init__(self,name,petals,price): #Initializer of flower
        self.name=None  #Init a nonetype value incase raising error when using the variable.
        self.petals=None  #Init a nonetype value incase raising error when using the variable.
        self.price=None #Init a nonetype value incase raising error when using the variable.
        self.setValue(name,petals,price)

    def getName(self):  #a method to get the name of flower instance
        if self.name == None:   #Handle the case if name is not set yet
            print("Name is not set yet.")
        else:   #Retrieve the name
            return self.name

    def getNumOfPet(self):  #a method to get the number of petals of flower instance
        if self.petals == None:   #Handle the case if number of petals is not set yet
            print("Number of petals is not set yet.")
        else:   #Retrieve the number of petals
            return self.petals

    def getPrice(self): #a method to get the price of flower instance
        if self.price == None:  #Handle the case if price is not set yet
            print("Price is not set yet.")
        else:   #Retrieve the price
            return self.price

    def setName(self,name): #A method to set the name of flower instance
        if str(type(name))!="<class 'str'>":    #Handle the case that input is not a string
            print("The input of the name is incorrect. A string is required")
            raise TypeError
        else:
            self.name = name    #Set name

    def setNumOfPet(self,petals): #A method to set the number of petals of flower instance
        if str(type(petals))!="<class 'int'>":    #Handle the case that input is not an int
            print("The input of the number of petals is incorrect. An integer is required")
            raise TypeError
        else:
            self.petals = petals
            

    def setPrice(self,price):   #a method to get the price of flower instance
        if str(type(price))!="<class 'float'>": #Handle the case that input is not a float
            print("The input of the price is incorrect. A float is required")
            raise TypeError
        else:
            if price*100%1==0:  #Handle the case that input has no more than 2 digits in the fractional part
                self.price = price
            else:
                print("Input price should not have more than 2 digits in the fractional part.")
                raise ValueError

    def setValue(self,name=False,petals=False,price=False): #a method to set all value of flower instance
        try:    #Only report the first type error
            if name:
                self.setName(name)
            if petals:
                self.setNumOfPet(petals)
            if price:
                self.setPrice(price)
        except:
            pass

    def getValue(self): #a method to get all value of flower instance
        output=dict()   #return the values in a dict var
        output["name"]=self.getName()
        output["numPetal"]=self.getNumOfPet()
        output["price"]=self.getPrice()
        return output