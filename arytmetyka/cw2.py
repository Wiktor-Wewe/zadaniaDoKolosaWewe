"""
zsumuj reszte z dzielenia przez 3 liczb od 1 do 100
"""

def f():
    suma = 0
    for x in range(1, 101):
        suma += x%3
    return suma
        
print(f())
