import matplotlib.pyplot as  plt
import numpy as np
import seaborn as sns

etykiety = ['A', 'B', 'C', 'D', 'E']
wartosci = [24, 96, 17, 66, 23]
kolory = ['plum', 'lightblue', 'steelblue', 'darkred', 'burlywood']
sns.set()
sns.set_style("white")
plt.barh(etykiety, wartosci, color=kolory)
plt.title('Wykres słupki')
plt.yticks(rotation=45)
plt.savefig('zad1.pdf')
