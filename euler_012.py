import sys
import math
#sys.setrecursionlimit(maxLimit)
#apparently this ^ is a "bad idea"

def make_triangle(n):
    # t = 0
    # for i in range(n):
    #     t += i
    t = n*(n+1)/2
    return t

def count_factors(t):   #put in triangle t, factor f, number of factors m
    m = 0   #first factor is f = t, t = t*1
    for f in range(int(math.sqrt(t))):
        if f == 0:
            pass
        elif t%f == 0:
            m +=2
        if f*f == t:
            m -=1
    return m

n = 106
print make_triangle(7)
m = 0
#print 'there are ', count_factors(t), ' factors in ', t
while m < 500:
    #t = make_triangle(n)
    if n%2 ==0:
        m = count_factors(n/2)*count_factors(n+1)
    else:
        m = count_factors((n+1)/2)*count_factors(n)
    n = n + 1
    #print n, m
print 'there are ', m, ' factors in ', n*(n+1)/2, ', the ', n, 'th triangle number'
