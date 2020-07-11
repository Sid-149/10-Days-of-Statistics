# Enter your code here. Read input from STDIN. Print output to STDOUT
def gm(n, p):
    q = 1-p
    return ((q**(n-1))*p)


prob = list(map(int, input().split()))
n = int(input())
p = prob[0]/prob[1]
s = 0
for i in range(n):
    s = s + gm(i+1, p)
print('%.3f' % s)
