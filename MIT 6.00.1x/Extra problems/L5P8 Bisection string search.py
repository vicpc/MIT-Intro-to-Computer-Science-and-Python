char = 'c'
aStr = 'abcdefghijklmnopqrstuvwxyz'

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    #Base case: if string is empty, returns False
    if aStr == '':
        return False
    
    #Base case: if string is length 1, returns the character
    if len(aStr) == 1:
        return aStr == char
        
    #Base case: if character is the middle character, returns True
    middle = len(aStr)/2 
    middleChar = aStr[middle]
    if char == middleChar:
        print "Found the character! " + char
        return True
    
    #Recursive case: if the character is in the lower bound of the string
    #recursively returns the function with the lower half of aStr
    elif char < middleChar:
        return isIn(char, aStr[:middle])
        
    #Otherwise recursively returns the function with the upper half of aStr
    else:
        return isIn(char, aStr[middle+1:])
        
isIn(char, aStr)