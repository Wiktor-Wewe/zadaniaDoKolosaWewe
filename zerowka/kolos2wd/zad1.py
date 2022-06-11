import matplotlib.pyplot as  plt
import numpy as np
import seaborn as sns

sns.set(style='whitegrid')
x = np.arange(0, 3*np.pi)
y1 = x + np.exp(1)
y2 = -4*x + 2
y3 = 2*np.cos(x)

w1 = sns.lineplot(data = y1, color='red')
w2 = sns.lineplot(data = y2, color='blue')
w3 = sns.lineplot(data = y3, color='yellow')
plt.title("Wykresy funkcji")
plt.legend()
plt.savefig("zad2.png")