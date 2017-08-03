import numpy as np
def checkNum(num):
    # if num%2 ==0:
    #     return False
    i = 3
    while i < (np.sqrt(num)+1):
        if num%i == 0:
            return False
        i += 2
    return True

prime_sum = 2
num = 3
while num < 2000000:
    #print num
    prime = checkNum(num)
    if prime:
        prime_sum += num
    num += 2
print prime_sum
