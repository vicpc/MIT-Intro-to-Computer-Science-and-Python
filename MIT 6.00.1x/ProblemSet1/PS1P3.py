#Problem 3: Alphabetical Substrings

#Write a function called item_order that takes as input a string named order. 
#The string contains only words for the items the customer can order separated by one space. 
#The function returns a string that counts the number of each item 
#and consolidates them in the following order:
#  salad:[# salad] hamburger:[# hambruger] water:[# water]

#If an order does not contain an item, then the count for that item is 0. 
#Notice that each item is formatted as [name of the item][a colon symbol][count of the item] 
#and all item groups are separated by a space.

#For example
#If order = "salad water hamburger salad hamburger" then the function returns "salad:2 hamburger:2 water:1"
#If order = "hamburger water hamburger" then the function returns "salad:0 hamburger:2 water:1"


#in canopy: line 40: print instead of return
#in MIT compiler: line 40: return instead of print
order = 'water salad salad hamburger water'
def item_order(order):
    water = 'water'
    salad = 'salad'
    hamburger = 'hamburger'
    numSalad = 0
    numHamburger = 0
    numWater = 0
   
    for i in range(len(order)):
        if order[i:i+len(water)] == water:
            numWater += 1
    
    for i in range(len(order)):
        if order[i:i+len(salad)] == salad:
            numSalad += 1
    
    for i in range(len(order)):
        if order[i:i+len(hamburger)] == hamburger:
            numHamburger += 1
        
    print "salad:" + str(numSalad) + " hamburger:" + str(numHamburger) + " water:" + str(numWater)
item_order(order)
