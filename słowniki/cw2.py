"""
zadeklaruj słownik za pomocą list comprehension (tutaj akurat dict a nie list)
"""

l = ["dupa", "chuj", "ziemniaki"]
w = ["tak", "srak", "ptak"]

s = {var: var2 for var, var2 in zip(l, w)}
print(s)
