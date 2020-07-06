# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

N = int(input())
X = list(map(int,input().split(' ')))

#for mean:
Mean = sum(X)/len(X)

sum1 = list()
for i in X:
    sum1.append((i-Mean)**2)

sum2 = sum(sum1)
sd = math.sqrt(sum2/N)

print("%.1f" % sd)
 
