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
per = x[0]/100
tot = x[1]
'''
p = 12/100
n = 10

#more than 2 rejects
s = 0
for i in range(n):
    if i < 3:
        s = s + binom(i, n, p)
print('%.3f' % s)

#atleast 2 rejects
s = 0
for i in range(n):
    if i > 1:
        s = s + binom(i, n, p)
print('%.3f' % s)
