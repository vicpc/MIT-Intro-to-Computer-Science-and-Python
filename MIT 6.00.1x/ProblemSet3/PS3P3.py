secretWord = "blue"
lettersGuessed = ['b', 'l', 'q', 'e', 'r', 's']


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    result = []
    
    #for all letters in secretWord
    for letter in secretWord:
        #if any of those letters are also in lettersGuessed
        if letter in lettersGuessed:
            #add that letter to result
            result += letter
        else:
            #otherwise add a '_'
            result += '_'

    print ' '.join(result)
   
getGuessedWord(secretWord, lettersGuessed) 