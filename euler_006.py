import numpy as np

a = 0
b = 0
for i in range(101):
    a = a + i**2    #sum of squares
    b = b + i   #just the sum
b = b**2

print "a", a
print "b", b
print "diff", b - a
