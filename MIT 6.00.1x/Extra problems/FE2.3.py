#write a program that examines three variables, x, y, z and prints the largest odd number among them

x = 3
y = 11
z = 9

if x%2 != 0:
    if x > y and x > z:
        print "x is the largest odd number"
    elif y%2 != 0:
        if y > x and y > z:
            print "y is the largest odd number"
        elif z%2 != 0:
            if z > y and z > x:
                print "z is the largest odd number"
        