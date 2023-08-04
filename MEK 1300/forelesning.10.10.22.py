
"""
def qr (x,y):
    q = x//y
    r = x % y

    return(q,r)


a = 10
b = 3
quit, rem = qr(a,b)

print(quit,rem)
"""

"""
def tota (*values):
    reuslt = 0
    for num in values:
        result = result + num
    return result

x = total (10, 20,30 )

print(x)
"""

#oppg1
"""
eks_liste = [1,53,23,42,13,23]

def average (liste):
    total = 0
    for item in liste:
        total += item
    return total/len(liste)
print(average(eks_liste))
print(min(eks_liste))

print(max(eks_liste))
"""
#oppg 2
"""
def listeprint():
    liste = []
    for i in range(10):

        liste.append(int(input()))
    for x in liste:
        print(liste[-x])

listeprint()
"""
#oppg3

liste = []

for i in range(5):
    liste.append(int(input("Enter a number")))

def funkt(l):
    mt = (*l,)
    for i in range(len(l)):
        l.pop(i)
        l.insert(i,mt[i-1])
        
funkt(liste)
print(liste)

