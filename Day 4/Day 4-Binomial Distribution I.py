# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(i):
    if i<=1:
        return 1
    else:
        return i*fact(i-1)

def binom(x, n, p):
    nCx = fact(n)/(fact(x)*fact(n-x))
    return (nCx*(p**x)*((1-p)**(n-x)))

'''
x = list(map(float, input().split()))
b = x[0]
g = x[1]
'''
b = 1.09
g = 1

p = b/(b+g)
n = 6
tot_prob = binom(3, n, p) + binom(4, n, p) + binom(5, n, p) + binom(6, n, p)
print('%.3f' % tot_prob)
