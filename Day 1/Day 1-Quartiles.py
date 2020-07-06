'''import numpy as np

n = int(input())
x = list(map(int, input().split(' ')))

if n % 2 != 0:
    q2 = np.median(x)
    pos = x.index(q1)
    x1 = x[:pos]
    x2 = x[pos+1:]
    q1 = np.median(x1)
    q3 = np.median(x2)
else:
    q2 = np.median(x)
    x1 = x[:int(n/2)-1]
    x2 = x[int(n/2)+1:]
    q1 = np.median(x1)
    q3 = np.median(x2)

print(int(q1))
print(int(q2))
print(int(q3))
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int, input().split(' ')))
x.sort()
if n % 2 != 0:
    q2 = x[int(n/2)]
    pos = x.index(q2)
    x1 = x[:pos]
    n1 = len(x1)
    x2 = x[pos+1:]
    n2 = len(x2)
    if n1 % 2 != 0:
        q1 = x1[int(n1/2)]
    else: q1 = (x1[int(n1/2)-1] + x1[int(n1/2)])/2
    if n2 % 2 != 0:
        q3 = x2[int(n2/2)]
    else: q3 = (x2[int(n2/2)-1] + x2[int(n2/2)])/2
else:
    q2 = (x[int(n/2)-1] + x[int(n/2)])/2
    x1 = x[:int(n/2)]
    x2 = x[int(n/2):]
    n1 = len(x1)
    n2 = len(x2)
    if n1 % 2 != 0:
        q1 = x1[int(n1/2)]
    else: q1 = (x1[int(n1/2)-1] + x1[int(n1/2)])/2
    if n2 % 2 != 0:
        q3 = x2[int(n2/2)]
    else: q3 = (x2[int(n2/2)-1] + x2[int(n2/2)])/2

print(int(q1))
print(int(q2))
print(int(q3))
