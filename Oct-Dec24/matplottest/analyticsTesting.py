
import csv
from functools import total_ordering

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook

import pandas as pd

df = pd.read_csv("vgchartz.csv")

scores = []

for x in df["critic"]:
    if not np.isnan(x):
        y = int(x * 10)
        scores.append(y)
    else:
        scores.append("")

df["percent"] = scores

clean_vgc = df[(df["percent"] != "")]

ship = []

for x in clean_vgc["shipped"]:
    if not np.isnan(x):
        ship.append(x)
    else:
        ship.append("")


y = 0

rows = clean_vgc.index

for x in clean_vgc["total"]:
    if np.isnan(x):
        clean_vgc.loc[rows[y], "total"] = ship[y]
    y += 1

clean_vgc.to_csv("clean_vgc.csv")


def average_sales_metacritic(df, score):
    shipped_df = df[(df["critic"] == score)
                    & (df["shipped"] != "")]
    totals_df = df[(df["critic"] == score)
                    & (df["total"] != "")]
    other_df = df[(df["critic"] == score)
                  & (df["total"] == "")]

    smean = shipped_df["shipped"].mean()
    tmean = totals_df["total"].mean()
    omean = (other_df["america"].mean() + other_df["europe"].mean() + other_df["japan"].mean() + other_df["other"].mean())

    return (smean + tmean + omean)/3

means = []
for i in np.arange(0, 10.1, 0.1):
    means.append(average_sales_metacritic(df, i))

plt.plot(means)
plt.show()



f = open("vgchartz.csv")
reader = csv.DictReader(f)
tb=[]
for row in reader:
    tb.append(row)


def total(a, e, j, o):
    tot = 0
    sales = [a, e, j, o]
    for i in sales:
        if i != "":
            temp = float(i)
            tot += temp
    print(type(tot))
    return tot


jp_sales = []
us_sales = []
total_sales = []


for row in tb:
    if row["america"] != "" and row["japan"] != "":
        if row["america"] != "0.0" and row["japan"] != "0.0":
            jp_sales.append(float(row["japan"]))
            us_sales.append(float(row["america"]))
            total_sales.append(total(row["america"], row["europe"], row["japan"], row["other"]))


plt.plot(jp_sales, us_sales, 'ro')
plt.axis((0, 2.5, 0, 10))
plt.xlabel('Japan Sales')
plt.ylabel('US Sales')
plt.show()

plt.scatter(jp_sales, us_sales)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()

print("hello")