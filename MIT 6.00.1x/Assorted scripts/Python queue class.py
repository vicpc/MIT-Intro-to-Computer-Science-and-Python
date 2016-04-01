class Queue(object):    
    '''
    Queue class with methods for adding and removing elements. 
    Will return a ValueError if the list is empty.
    '''

    def __init__(self):
        '''Initializes 1 attribute: a list to keep track of the queue's elements'''
        self.qlist = []
        
    def insert(self, element):
        '''Uses the append method to add an element to the attribute list'''
        self.qlist.append(element)
                    
    def remove(self):
        '''Removes an element from the list'''
        
        #If list empty, raise ValueError
        if self.qlist == []:
            raise ValueError()
        
        #Pops an element from the front of the list, returns list
        else:
            return self.qlist.pop(0)
