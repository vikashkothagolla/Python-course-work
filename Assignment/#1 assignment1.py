n=5
for i in range(n):
    print(' ' * (n - i - 1) + ' * ' * ( i+1))
for i in range(n-2-i-1):
     print(' ' * (n - i - 1) + ' * ' * ( i+1))

