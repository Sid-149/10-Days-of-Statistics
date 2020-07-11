# Enter your code here. Read input from STDIN. Print output to STDOUT

def fact(i):
    if i<=1:
        return 1
    else:
        return i*fact(i-1)

def poisson(k, lamda):
    e = 2.71
    num = (lamda**k)*(e**(-lamda))
    den = fact(k)
    return num/den

lamda = float(input())
k = int(input())
print('%.3f' % poisson(k, lamda))
