import math

x = float(input('insert the x value: '))

if -1<x<1:
    
    previousEl = 1
    currentEl = -1*x/2
    approxSum = previousEl + currentEl
    ACCURACY = 10**(-6)
    n = 1

    while abs(currentEl - previousEl) > ACCURACY:
        n += 1
        previousEl = currentEl
        currentEl = (math.factorial(2*n-1)*((-1)**n)*(x**n))/(2**(2*n-1)*math.factorial(n-1)*math.factorial(n))
        approxSum += currentEl
        print(' n=%-3d current=%13.10f' % (n, currentEl))
    print('шукане:', approxSum)

else:
    print('err')