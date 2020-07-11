# Enter your code here. Read input from STDIN. Print output to STDOUT
lamda = list(map(float, input().split()))
lambda1 = lamda[0]
lambda2 = lamda[1]

print ('%.3f' % (160 + 40 * (lambda1 + lambda1 ** 2)))
print ('%.3f' % (128 + 40 * (lambda2 + lambda2 ** 2)))
