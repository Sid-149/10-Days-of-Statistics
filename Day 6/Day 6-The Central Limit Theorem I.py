# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

tot_pounds = int(input())
n = int(input())
mean = int(input())
std = int(input())

mean1 = mean * n
std1 = math.sqrt(n) * std

print ('%.4f' % (cumulative(mean1, std1, tot_pounds)))
