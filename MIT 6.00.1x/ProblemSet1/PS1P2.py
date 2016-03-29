#Problem 2: Counting 'bob's

#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print
    #Number of times bob occurs is: 2
#For problems such as these, do not include raw_input statements or define the variable s in any way. 
#Our automating testing will provide a value of s for you - 
#so the code you submit in the following box should assume s is already defined. 
#If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

s = 'azcbobobegghakl'
numBob = 0
myString = 'bob'
 
for i in range(len(s)):
   if s[i:i+len(myString)] == myString:
       numBob += 1     
               
print str(numBob)
    
#make an index range(s)? Can you do this with string? Yes with "range(len(string))"
#for each index iterate the string, checking for 'bob'
#for each bob found count += 1


