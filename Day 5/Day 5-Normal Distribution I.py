# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumulative(mean, std, val):
    return 0.5 * (1 + math.erf((val - mean) / (std * (2 ** 0.5))))

mean_std = list(map(float, input().split()))
mean = mean_std[0]
std = mean_std[1]
period1 = float(input())
period2 = list(map(float, input().split()))

print ('%.3f' % (cumulative(mean, std, period1)))
print ('%.3f' % (cumulative(mean, std, period2[1]) - cumulative(mean, std, period2[0])))
