import numpy as np

a = 0
b = 0

def check_palindrome(n):
    n = str(n)
    m = n[::-1]
    pal = False
    if m == n:
        pal = True
    return pal

palindrome = 0
for j in range(1000):
    for k in range(1000):
        product = j*k
        pal = check_palindrome(product)
        if (pal == True) and (product > palindrome):
            palindrome = product
print palindrome
