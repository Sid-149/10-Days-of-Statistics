# Enter your code here. Read input from STDIN. Print output to STDOUT

def rank(a):
    rank = {}
    sort = sorted(a)
    for i in range(len(a)):
        for j in range(len(sort)):
            if a[i] == sort[j]:
                rank[a[i]] = j + 1
    return rank

def spearman(x, y, rx, ry, n):
    diff_rank = list()
    for i in range(n):
        if rx[x[i]] != ry[y[i]]:
            diff_rank.append((rx[x[i]] - ry[y[i]]) ** 2)
    return (6 * sum(diff_rank)) / (n ** 3 - n)

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rank_X = rank(X)
rank_Y = rank(Y)

rxy = spearman(X, Y, rank_X, rank_Y, n)
s = 1- rxy
print('%.3f' % s)
