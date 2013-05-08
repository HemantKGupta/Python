'''
Created on May 7, 2013

@author: HemantG
'''
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
print(str(iterPower(2,5)))