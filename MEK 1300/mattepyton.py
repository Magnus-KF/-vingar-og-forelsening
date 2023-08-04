x0 = 5
x = x0
toleranse = 1E-5

def f(x):
    return x**2 -4

def fder(x):
    return 2*x

while toleranse < abs(f(x)):
    x = x -f(x)/fder(x)

print(x)