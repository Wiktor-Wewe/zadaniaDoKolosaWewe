import matplotlib.pyplot as  plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('whitegrid')

x = np.arange(0.5, 10, 0.5)
y1 = np.log(2*x)
y2 = -4*x+2
y3 = 2*np.cos(x)

plt.plot(x, y1, label = 'y = log(2x)', color = 'blue', marker = '^')
plt.plot(x, y2, label = 'y = -4x+2', color = 'red', marker = 'o')
plt.plot(x, y3, label = 'y = 2cos(x)', color = 'pink', marker = 's')
plt.legend()
plt.title('Bardzo fajny wykres')
plt.xlabel('przedzial od 0.5 do 10')
plt.ylabel('wartosci poszczegolnych funkcji')
#plt.show()
plt.savefig('zad1.png')
