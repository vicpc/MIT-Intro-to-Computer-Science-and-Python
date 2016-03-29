# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import sys 
import re

WORDLIST_FILENAME = "/Users/macbookpro/Desktop/Learning/Data_Science/Python/6.00.1x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

secretWord = 'blue'
mistakesMade = 0
result = []

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


def getGuessedWord(secretWord, lettersGuessed, result):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    #for all letters in secretWord
    for letter in secretWord:
        
        #if any of those letters are also in lettersGuessed
        if letter in lettersGuessed:
            #add that letter to result
            result += letter
        '''
        else:
            #otherwise add a '_'
            result += '_'
        '''
    print ' '.join(result)

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
    print 'Available letters: ' + ''.join(result)
    

def hangman(secretWord, mistakesMade):
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
    
    print "The secret word containts " +str(len(secretWord)) + " letters"
    
    #Guess count variable 
    mistakesLeft = 8 - mistakesMade
                
    while mistakesMade < 8:
                
        #User input Guess
        guess = raw_input("Guess a letter... ")
        lettersGuessed = ''
    
        #Conditions on guess, see regular expressions: https://docs.python.org/2/library/re.html        
        if not re.match("^[a-z]*$", guess): 
            guess = raw_input("Only a-z letters allowed! ")
            sys.exit()
        elif len(guess) != 1:
            guess = raw_input("Guess only one letter... ")
            sys.exit()
    
        guessInLower = guess.lower() #converts to lower case
        
        #this is wrong, needs to be added only if True
        lettersGuessed += guessInLower #adds guess to lettersGuessed list        
        
        if guessInLower in secretWord:
            print "Correct! ------ is in the secret word."
        else: 
            print "Wrong! ------ is not in the secret word " + str(mistakesLeft) + " mistakes left."
            #need to update lettersGuessed here?
            mistakesMade += 1
            print "Mistakes: " +str(mistakesMade) + "... (8 total allowed)" 
       
        #Fix this to print result join with no space 
        getGuessedWord(secretWord, lettersGuessed, result) #prints letter if guessed 
        getAvailableLetters(lettersGuessed) #available letters
        
        #If guessed the word ends game, otherwise plays another round
        #Not working? Need to set the string from lettersGuessed
        if isWordGuessed(secretWord, lettersGuessed): 
            print "You win!"
        else:
            hangman(secretWord, mistakesMade)
    
    if mistakesMade >= 8:
        print "You lose!"
            
hangman(secretWord, mistakesMade)
      
    #mistakesMade = number of incorrect guesses so far
    #secretWord = The word to guess
    #lettersGuessed = letters that have been guessed so far
    #availableLetters = Letters that may still be guessed
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
