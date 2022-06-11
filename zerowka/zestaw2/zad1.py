import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('white')

etykiety = ['A', 'B', 'C', 'D', 'E']
wL = np.array([35, 47, 15, 40, 39])
wP = np.array([-30, -32, -38, -33, -30])

kolL = ['skyblue', 'pink', 'tomato', 'grey', 'indigo']
kolP = ['violet', 'cyan', 'aqua', 'rosybrown', 'olive']

plt.subplot(1, 2, 1)
plt.barh(etykiety, wL, color = kolL)
plt.title('Wykres lewy')
plt.xticks(np.arange(0, 41, step = 10))

plt.subplot(1, 2, 2)
plt.barh(etykiety, wP, color = kolP)
plt.title('Wykres prawy')
plt.xticks(np.arange(0, -31, step = -10))

plt.savefig('zad1.png')
