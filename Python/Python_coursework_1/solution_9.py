'''5! = 5*4*3*2*1'''

n= int(input("enter factorial number: "))

def factoriaL(n):
    if n < 0:
        return "it's a negative number"
    fact = 1
    for j in range(2, n + 1):
        fact = fact * j

    return fact


print(factoriaL(n))