# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

m, n = map(int, input().split())
X = list()
Y = list()

for i in range(n):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        if j < m:
            x.append(elements[j])
        else:
            Y.append(elements[j])
    X.append(x)

#source: https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial
model = linear_model.LinearRegression()
model.fit(X, Y)
a = model.intercept_
b = model.coef_

q = int(input())
new_X = []
for i in range(q):
    x = [0]
    elements = list(map(float, input().split()))
    for j in range(len(elements)):
        x.append(elements[j])
    new_X.append(x)

result = model.predict(new_X)
for i in range(len(result)):
    print('%.2f' %result[i])
