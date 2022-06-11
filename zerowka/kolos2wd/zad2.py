import matplotlib.pyplot as  plt
import numpy as np
import pandas as pd

df = pd.read_excel('mieszkania22.xlsx')
print(df.groupby(['Formy budownictwa'])['Wartość'].mean())

print(df)
w_ind = df[df['Formy budownictwa'] == 'indywidualne']['Wartość']
w_spo = df[df['Formy budownictwa'] == 'spółdzielcze']['Wartość']
w_kom = df[df['Formy budownictwa'] == 'komunalne']['Wartość']
lata = df[df['Formy budownictwa'] == 'komunalne']['Rok']

plt.bar(lata, w_ind, label='Mieszkania indywidualne')
plt.bar(lata, w_spo, label='Mieszkania spółdzielcze')
plt.bar(lata, w_kom, label='Mieszkania komunalne')
plt.xlabel('lata')
plt.ylabel('wartość')
plt.title('Ceny poszczególnych form budowli')
plt.text(2014.6, 5000, '164439')
plt.legend()
plt.savefig('zad2.pdf')