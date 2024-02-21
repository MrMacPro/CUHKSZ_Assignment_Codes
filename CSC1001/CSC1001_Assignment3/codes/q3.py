import random
class Ecosystem:
    def __init__(self,river_length,num_fish,num_bears):
        #Initialize datafields
        self.riverLen=river_length
        self.numOfBear=num_bears
        self.numOfFish=num_fish

        self.numOfAnimal=0
        self.newlyCreated=[]

        #Initialize river status
        self.river=['N']*self.riverLen
        self.addAnimal(self.numOfBear,'B')
        self.addAnimal(self.numOfFish,'F')
    
    def addAnimal(self,num,type):  #num=self.numOfxxxx type='B'|'F'
        if num+self.numOfAnimal<=self.riverLen: #Only put if there is enough space
            self.numOfAnimal+=num  #Add newly added animal to total number
            for i in range(num): #Randomly put
                while True: #Randomly find an empty place
                    position=random.randint(0,self.riverLen-1)
                    if self.river[position]=='N':   #Put an animal here if it is empty
                        self.river[position]=type
                        self.newlyCreated.append(position)
                        break

    def __str__(self):  #Output the ecosystem status by printing a sequence including 'N','B', and 'F'
        output=''
        for i in self.river:
            output+=i   #Translate list into string
        return output

    def simulate(self,steps): #Simulation Method
        print(self)
        for iteration in range(steps):  #Do the simulation N times
            self.newlyCreated=[]
            for i in range(self.riverLen):    #Operate movement by element
                if i in self.newlyCreated:
                    continue
                if self.river[i]=='B':
                    self.bearBehaviour(i)
                elif self.river[i]=='F':
                    self.fishBehaviour(i)
            print(self)

    def bearBehaviour(self,currentPos): #Each operation for a bear
        nextPos=random.randint(currentPos-1,currentPos+1)
        if nextPos<0 or nextPos>=self.riverLen: #Disappear if the target location is out of range
            self.river[currentPos]='N'
            return
        if self.river[nextPos]=='B' and nextPos!=currentPos:    #Add a new bear if it is about to collide in another bear
            self.addAnimal(1,'B')
        else:   #Overwrite the target position if it is empty or a fish
            self.newlyCreated.append(nextPos)
            self.river[currentPos]='N'
            self.river[nextPos]='B'

    def fishBehaviour(self,currentPos): #Each operation for a bear
        nextPos=random.randint(currentPos-1,currentPos+1)
        if nextPos<0 or nextPos>=self.riverLen: #Disappear if the target location is out of range
            self.river[currentPos]='N'
            return
        if self.river[nextPos]=='N':    #Go to target position if it is empty
            self.river[nextPos]='F'
            self.newlyCreated.append(nextPos)
            self.river[currentPos]='N'
        elif self.river[nextPos]=='B':  #Disappear if it is a bear
            self.river[currentPos]='N'
        elif self.river[nextPos]=='F' and nextPos!=currentPos:  #Add a new fish if it is about to collide  in another bear
            self.addAnimal(1,'F')

if __name__=="__main__" :
    # Test 1
    ecosystem = Ecosystem(river_length=3, num_fish=1, num_bears=1)
    ecosystem.simulate(steps=2)

    # Test 2
    ecosystem = Ecosystem(river_length=10, num_fish=3, num_bears=2)
    ecosystem.simulate(steps=5)

    # Test 3
    ecosystem = Ecosystem(river_length=8, num_fish=2, num_bears=1)
    ecosystem.simulate(steps=10)

    # Test 4
    ecosystem = Ecosystem(river_length=10, num_fish=2, num_bears=3)
    ecosystem.simulate(steps=10)