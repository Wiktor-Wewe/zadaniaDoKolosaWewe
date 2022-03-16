"""
przesuń napis o n znaków, czyli jeśli napis="ala"  n=1, to napis="laa"
"""

def f(n, napis):
    n = n%len(napis)
    nowyNapis = ""
    for x in range(n, len(napis)):
        nowyNapis += napis[x]
    for x in range(0, n):
        nowyNapis += napis[x]
    return nowyNapis

print(f(11, "ala"))
        
