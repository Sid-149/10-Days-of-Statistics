# Enter your code here. Read input from STDIN. Print output to STDOUT

def gm(n, p):
    q = 1-p
    return ((q**(n-1))*p)


prob = list(map(int, input().split()))
n = int(input())
p = prob[0]/prob[1]
print('%.3f' % gm(n,p))
