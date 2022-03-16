"""
napisz program który sprawdzi wartość funkcji charakterystycznej dla n i zbioru A
"""

def f(n, A):
    if n in A:
        return True
    return False

print(f(2, [1, 2, 3, 4, 5]))
