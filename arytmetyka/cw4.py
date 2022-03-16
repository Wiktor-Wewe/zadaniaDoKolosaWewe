"""
Sprawdź czy trójkąt o podanych przez użytkownika bokach może istnieć
"""

a = int(input())
b = int(input())
c = int(input())

def pitaChuj(a, b, c):
    if a>b and a>c :
        if b**2+c**2 == a**2:
            return True
        else:
            return False
    elif b>a and b>c:
        if a**2 + c**2 == b**2:
            return True
        else:
            return False
    elif c>a and c>b:
        if a**2 + b**2 == c**2:
            return True
        else:
            return False
    else:
        return False

print(pitaChuj(a, b, c))
