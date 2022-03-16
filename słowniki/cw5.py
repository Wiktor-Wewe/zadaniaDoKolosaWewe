"""
wygeneruj losowy słownik
"""
from random import randint
s = {str(randint(1, 20)): randint(1, 20) for _ in range(0, randint(2, 20))}
print(s)
