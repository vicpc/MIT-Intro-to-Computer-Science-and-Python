secretWord = 'Blue'
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.
      
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #imports regular expressions
    import re
     
    print "The secret word containts " +str(len(secretWord)) + " letters"
    
    #User input Guess
    guess = raw_input("Guess a letter... ")
    
    #Conditions on guess, see regular expressions: https://docs.python.org/2/library/re.html
    if not re.match("^[a-z]*$", guess): 
        guess = raw_input("Only a-z letters allowed! ")
        sys.exit()
    elif len(guess) != 1:
        guess = raw_input("Guess only one letter... ")
        sys.exit()
    guess.lower() #converts to lower case

    '''
    
    '''    
    
    
    print guess
    
    #mistakesMade = number of incorrect guesses so far
    #secretWord = The word to guess
    #lettersGuessed = letters that have been guessed so far
    #availableLetters = Letters that may still be guessed
    
hangman(secretWord)