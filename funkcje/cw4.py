"""
zadeklaruj funkcję która zwraca pierwiastki całkowite z zakresu (1,10〉
"""
from math import sqrt
def f():
    t = []
    for x in range(1, 11):
        if sqrt(x) == int(sqrt(x)):
            t.append(x)
        return t
    
print(f())
