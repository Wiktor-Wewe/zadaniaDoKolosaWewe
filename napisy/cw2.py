"""
napisz program który sprawdzi czy w podanym ciągu znaków znajduje się znak polski
"""

def f(s):
    t = ['ą', 'ć', 'ó'] #"wszystkie polskie znaki"
    for x in t:
        if x in s:
            return True
    return False

print(f("chuj"))
