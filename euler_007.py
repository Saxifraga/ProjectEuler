import numpy as np

# primes = []
def checkNum(num):
    # for i in range(2,num):
    #     if num%i ==0:
    #         return False
    #     else:
    #         pass
    # return True
    if num%2 ==0:
        return False
    i = 3
    while i < (np.sqrt(num)+1):
        if num%i == 0:
            return False
        i += 2
    return True


# while len(primes) < 10002:
count = 1
num = 2
#prime = False
while count < 10001:
    print 'this iter ', count
    prime = checkNum(num)
    if prime == True:
        count += 1
    num += 1
print 'prime number ', count
print 'the number is ', num - 1
