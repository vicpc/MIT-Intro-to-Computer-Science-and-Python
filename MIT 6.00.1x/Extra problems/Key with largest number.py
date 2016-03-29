#Returns keys corresponding to entry with largest number of values associated to it.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print animals.keys()

def biggest(animals):
    
    result = None
    biggestValue = 0
    
    #for number of times a key is counted
    for i in animals.keys():
        
        #prints the keys
        #print i 

        #if amount for each given key is bigger than biggest value counter
        if len(animals[i]) >= biggestValue: 
            
            #stores key with highest value
            result = i
            
            #i is now set to the value of the key with the highest value
            #prints  anumber
            biggestValue = len(animals[i])
    
    #Prints the key with highest vaue    
    print result
biggest(animals)

    