X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]
n = len(X)
mean_x = sum(X)/len(X)
mean_y = sum(Y)/len(Y)
mul_xy = list()
for i in range(n):
    mul_xy.append(X[i]*Y[i])

square_x = list()
for i in range(n):
    square_x.append(X[i]**2)
num = (n*sum(mul_xy))-(sum(X)*sum(Y))
den = (n*sum(square_x))-(sum(X)**2)
b = num/den
a = mean_y - b*mean_x
x = 80
y = a + b*x
print('%.3f' %y)
