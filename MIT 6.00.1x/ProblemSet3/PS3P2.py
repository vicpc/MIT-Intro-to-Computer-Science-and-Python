secretWord = 'blue'
lettersGuessed = ['b', 'l', 'q', 'e', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    secretWordSet = set(secretWord)
    lettersGuessedSet = set(lettersGuessed)

    #print set(secretWord)
    # >>> prints set(['e', 'b', 'u', 'l'])

    if secretWordSet.issubset(lettersGuessedSet):
        return True
    else:
        return False

isWordGuessed(secretWord, lettersGuessed)
