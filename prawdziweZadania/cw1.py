"""
Zsumuj wszystki liczby dzielące się przez 3 lub 5 poniżej 1000
odp:234168
"""

def f():
    suma = 0
    for x in range(1001):
        if x%3==0 or x%5==0:
            suma += x
    return suma

print(f())
