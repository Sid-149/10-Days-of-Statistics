# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

n = int(input())
mean = int(input())
std = int(input())
per = float(input())
val = float(input())

ci = val * (std / math.sqrt(n))

print('%.2f' %(mean - ci))
print('%.2f' %(mean + ci))
