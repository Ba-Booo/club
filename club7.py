def factorial(i):

    for a in range( 1, int(i) ):

        i = int(i) + a
        
    return i

print( factorial( input() ) )