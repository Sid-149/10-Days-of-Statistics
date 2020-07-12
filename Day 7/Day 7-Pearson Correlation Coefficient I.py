# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stats
def pearson(n, X, Y):
    a = list()
    mean_X = stats.mean(X)
    mean_Y = stats.mean(Y)
    std_X = stats.pstdev(X)
    std_Y = stats.pstdev(Y)
    for i in range(n):
        a.append((X[i]-mean_X)*(Y[i]-mean_Y))
    return (sum(a)/(n*std_X*std_Y))

n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))
print('%.3f' % pearson(n ,X, Y))
