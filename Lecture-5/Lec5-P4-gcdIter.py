'''
Created on May 7, 2013

@author: HemantG
'''
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = 1
    if a > b:
        test = b
    else:
        test = a
    while not(a%test == 0 and b%test ==0):
        
        if test == 1:
            break
        else:
            test -=1            
    return test
print(str(gcdIter(10,3)))
print(str(gcdIter(12,4)))