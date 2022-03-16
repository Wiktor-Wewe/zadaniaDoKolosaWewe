"""
Znajdz najmniejszą liczbę, która dzieli się przez liczby od 1 do 20
odp: 232792560
"""

def a():
    l = 1
    while True:
        czyPodzielna = True
        for i in range(1, 21):
            if l%i!=0:
                czyPodzielna=False
                break
        if czyPodzielna:
            return l
        l+=1
print(a())
