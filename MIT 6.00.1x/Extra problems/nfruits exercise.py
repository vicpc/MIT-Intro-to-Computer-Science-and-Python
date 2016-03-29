fruits = {'A': 1, 'B': 2, 'C': 3}
pattern = 'AC'

def nfruits(fruits, pattern):
    '''
    fruits: non-empty dictionary containing the types of fruit and its quantities
    initially carried when leaving home. 
    pattern: A string pattern of the fruits eaten on the journey.
    
    returns the maximum quantity out of the different fruits that is available when
    destination is reached. 
    '''
    
    #Removes 1 for every fruit consumed
    pattern = list(pattern)
    for i in pattern:
        if i in fruits:
            fruits[i] -= 1
            
            #add +1 for every fruit not consumed
            if pattern.index(i) < len(pattern) - 1:
                for j in fruits:
                    if j != i:
                        fruits[j] += 1
    
    print max(fruits.values())

nfruits(fruits, pattern)

