import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./2020i2021/z2/nieruchomosci2.csv", sep=";").T
df = df.rename(columns={0: "metraż", 1: "rok", 2: "cena"}, index={"rynek pierwotny.1": "rynek pierwotny", "rynek pierwotny.2": "rynek pierwotny",
                                                                  "rynek pierwotny.3": "rynek pierwotny", "rynek wtórny.1": "rynek wtórny", "rynek wtórny.2": "rynek wtórny", "rynek wtórny.3": "rynek wtórny", })
df.reset_index(inplace=True)
df = df.rename(columns={"index": "rynek"})
df["cena"] = df["cena"].str.replace(" ", "")
df["cena"] = df["cena"].apply(pd.to_numeric)
wszystko = df["cena"].sum()
pogrupowane = df.groupby("rynek")["cena"].sum()
pogrupowane /= wszystko
plt.pie(pogrupowane, labels=df["rynek"].unique(),
        autopct='%1.1f%%')
plt.title("Procentowy zysk od metra w zależności od rynku w roku 2018")
plt.show()