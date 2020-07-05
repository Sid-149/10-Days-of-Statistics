N = int(input())
X = list(map(int,input().split(' ')))
W = list(map(int,input().split(' ')))

mul = list()

for i in range(N):
    mul.append(X[i]*W[i])

mw = sum(mul)/sum(W)

print("%.1f" % mw)
