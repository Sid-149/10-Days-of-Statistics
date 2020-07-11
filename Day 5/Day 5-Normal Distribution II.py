# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def cumulative(mean, std, val):
    return 0.5 * (1 + math.erf((val - mean) / (std * (2 ** 0.5))))

mean_std = list(map(float, input().split()))
mean = mean_std[0]
std = mean_std[1]
mean1 = int(input())
mean2 = int(input())

print ('%.2f' % (100 - cumulative(mean, std, mean1)*100))
print ('%.2f' % (100 - cumulative(mean, std, mean2)*100))
print ('%.2f' % (cumulative(mean, std, mean2)*100))
