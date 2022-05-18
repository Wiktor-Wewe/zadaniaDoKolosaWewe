import matplotlib.pyplot as  plt
import numpy as np
import seaborn as sns

sns.set()
sns.set_style('white')
etykiety = ['A', 'B', 'C', 'D', 'E']
kolory_wl = ['lightskyblue', 'pink', 'tomato', 'lavender', 'purple']
wl = np.array([35, 48, 15, 41, 40])
kolory_wp = ['violet', 'cyan', 'aqua', 'brown', 'olive']
wp = np.array([-30, -34, -39, -36, -30])

plt.subplot(1,2,1)
plt.xticks(np.arange(0, 41, step = 10))
plt.barh(etykiety, wl, color = kolory_wl)
plt.title("Wykres lewy")

plt.subplot(1,2,2)
plt.xticks(np.arange(0, -40, step = -10))
plt.barh(etykiety, wp, color = kolory_wp)
plt.title("Wykres prawy")
plt.savefig("zad1.png")
