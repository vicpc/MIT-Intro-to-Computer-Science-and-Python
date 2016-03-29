#Guessing Game 
#Bisection Search

low = 0
high = 100
guess = (low + high)/2
print "Think of a number between 0 and 100!"

#loop
while True:
    guess = (high + low) / 2
    print "Is your number higher or lower than " + str(guess) + """?
    Type 'h' for higher."
    Type 'l' for lower."
    Type 'c' for correct answer.
    """

    number = raw_input("h, l or c? ")
    if number == 'c':
        break
    elif number == 'h':
        low = guess
    elif number == 'l': 
        high = guess 
    else:
        print "I didn't understand your input. Please use h, l or c."
 
#Game over      
print "Game over. Your secret number was " + str(guess)
 
        
        
        

            
        