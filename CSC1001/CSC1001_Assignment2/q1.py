def sqrt(n):    #Define sqrt() function
    lastGuess=1 #Initialize lastGuess
    while True: #Use infinite loop to contiuously find more precise square root
        nextGuess=(lastGuess+n/lastGuess)/2 #Calculate nextGuess
        if -0.0001<nextGuess-lastGuess<0.0001:  #Test if the Guess converge to sufficiently small
            return int(nextGuess*10000)/10000    #Return the result and remain 4 digit on fractional part
        lastGuess=nextGuess #If not, keep finding