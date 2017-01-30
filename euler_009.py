import numpy as np

sum = 0
for i in range(2000000):
    prime = True
    notDone = True
    jmax = i
    j = 2
    while (prime == True)and(j<jmax):
        if i%j==0:
            prime = False
        j = j + 1

    if prime == True:
        sum +=i
print sum
