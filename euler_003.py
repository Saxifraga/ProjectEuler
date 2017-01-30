import numpy as np

n = 600851475143
#n = 13195
m = int(np.sqrt(n))
factors = []
prime_factors = []
for i in range(2,m):
    if n%(i) == 0:  #if anything is a factor of n
        factors.append(i)   #save it
        prime = True
        for j in range(2,i):
            # print 'factor', i, 'divisor', j
            # print 'remainder', i%j
            if i%j == 0: #if anything is a factor of i
                prime = False   #break out of the while loop and increment
        if prime == True:
            prime_factors.append(i)

print prime_factors
print 'for you, with love'
