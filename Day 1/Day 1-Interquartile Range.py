N = int(input())
X = list(map(int,input().split(' ')))
F = list(map(int,input().split(' ')))

x = list()

for i in range(N):
    while F[i] != 0:
        x.append(X[i])
        F[i] = F[i]-1

x.sort()
n = len(x)
if n % 2 != 0:
    q2 = x[int(n/2)]
    pos = x.index(q2)
    x1 = x[:pos]
    n1 = len(x1)
    x2 = x[pos+1:]
    n2 = len(x2)
    if n1 % 2 != 0:
        q1 = float(x1[int(n1/2)])
    else: q1 = (x1[int(n1/2)-1] + x1[int(n1/2)])/2.0
    if n2 % 2 != 0:
        q3 = float(x2[int(n2/2)])
    else: q3 = (x2[int(n2/2)-1] + x2[int(n2/2)])/2.0
else:
    q2 = (x[int(n/2)-1] + x[int(n/2)])/2.0
    x1 = x[:int(n/2)]
    x2 = x[int(n/2):]
    n1 = len(x1)
    n2 = len(x2)
    if n1 % 2 != 0:
        q1 = float(x1[int(n1/2)])
    else: q1 = (x1[int(n1/2)-1] + x1[int(n1/2)])/2.0
    if n2 % 2 != 0:
        q3 = float(x2[int(n2/2)])
    else: q3 = (x2[int(n2/2)-1] + x2[int(n2/2)])/2.0

diff = q3-q1
print("%.1f" % diff)
