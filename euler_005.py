import numpy as np

prime_product = 1*2*3*5*7*11*13*17*19

def check_factors(i):
    for k in range(1, 21):
        if i%k != 0:
            return False
    print "found it!!!", i
    return True

flag = False
i = prime_product
while flag == False:
    flag = check_factors(i)
    i = i + 1
