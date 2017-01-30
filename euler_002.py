last_fib = 0
lf = 1
evenfib = 0
fib = 0
while fib < 4000000:
  fib = lf + last_fib
  if fib%2 ==0:
    evenfib = evenfib + fib
  lf = last_fib
  last_fib = fib
print('sum', evenfib)
