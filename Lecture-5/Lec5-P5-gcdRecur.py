'''
Created on May 7, 2013

@author: HemantG
'''
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)
print(str(gcdRecur(10,3)))
print(str(gcdRecur(12,4)))