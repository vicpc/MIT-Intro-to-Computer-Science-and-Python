lettersGuessed = ['a', 'b', 'c', 'd']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    import string
    
    result = list(string.ascii_lowercase)
    
    #for all letters in lettersGuessed
    for letter in lettersGuessed:
        #if any of those letters are also in string.ascii_lowercase
        if letter in string.ascii_lowercase:
            #removes that letter from the list string.ascii_lowercase
            result.remove(letter)
    
    #joins the list of string into a single string
    print ''.join(result)

getAvailableLetters(lettersGuessed)
    