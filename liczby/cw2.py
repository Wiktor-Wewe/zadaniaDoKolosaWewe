"""
napisz program który zmieni int'a w string'a, doda na końcu część po przecinku i skonwertuje na floata
"""

def f(n):
    n = str(n)
    n+=".12"
    return float(n)

print(f(int(12)))
