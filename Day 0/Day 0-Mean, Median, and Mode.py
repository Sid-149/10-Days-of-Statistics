# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(int,input().split(' ')))
#print(X)
#for mean:
Mean = sum(X)/len(X)
print("%.1f" % Mean)

#for median:
X.sort()
#print(X)
if N % 2 == 0:
    Median = (X[int(N/2)-1] + X[int(N/2)])/2
else : Median = X[int(N/2)]
print("%.1f" % Median)

#for mode:
mode = dict()
for i in range(N):
    c = 0
    for j in range(N):
        if X[i] == X[j]:
            c  += 1
        mode[X[i]] = c
#print(mode)
all_val = list(mode.values())
max_value = max(all_val)
Mode = list(mode.keys())[all_val.index(max_value)]
print(Mode)

'''
import numpy as np
from scipy import stats

N = int(input())
X = list(map(int,input().split(' ')))

Mean = np.mean(X)
Median = np.median(X)
Mode = stats.mode(X)[0]

print("%.1f" % Mean)
print("%.1f" % Median)
print(Mode[0])

'''
