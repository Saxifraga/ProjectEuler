import numpy as np

n = 0
for i in range(1, 1700):
    if n == 1000.0:
        print 'pavlova'
        break
    for j in range(1, 1700):
        if n == 1000.0:
            print 'peachy keen'
            break
        k = i**2 + j**2
        l = np.sqrt(k)
        if k%int(l) == 0.0:
            n = i + j + l
            if n == 1000:
                print 'i', i, 'j', j, 'k', l
                print 'here is the product, bazam', i*j*k

# k = 201**2 + 376**2
# l = np.sqrt(k)
# print k%int(l)
# if k%int(l) == 0.0:
#     print 'bablabawieh'
