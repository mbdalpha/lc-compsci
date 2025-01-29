
import csv
from functools import total_ordering

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.cbook as cbook

import pandas as pd

fig, ax = plt.subplots()

## gives average sales for the metacritic score

def average_sales_metacritic(df, score, region):
    totals_df = df[(df["critic"] * 10 == score)
                    & (df[region])]
    mean = totals_df[region].mean()

    return mean


df = pd.read_csv("clean_vgc.csv")

regions = ["total", "america", "europe", "japan", "other"]
for r in regions:
    means = []
    for i in range(0, 101, 1):
        means.append(average_sales_metacritic(df, i, r)*1000000)
    if r == "total":
        line1 = ax.plot(means, label = "Total")
    if r == "america":
        line2 = ax.plot(means, dashes=[3, 1], label="America")
    if r == "europe":
        line3 = ax.plot(means, dashes = [6, 2], label = "Europe")
    if r == "japan":
        line4 = ax.plot(means, dashes = [2, 2, 10, 2], label = "Japan")
    if r == "other":
        line5 = ax.plot(means, dashes = [3, 3, 5, 2], label = "Other")


ax.legend()
ax.set_yscale('log')
ax.set_ylabel('total sales')
ax.set_xlabel('Average sales')
ax.set_title('Total video game sales in different regions')
plt.show()


## to figure out which region purchases the most video games
def total_sales_region(df, region):
    totals_df = df[(df[region] != "")]
    t = totals_df[region].sum()

    return t

regions = ["america", "europe", "japan", "other"]
totals = []
for i in regions:
    totals.append(total_sales_region(df, i))

ax.bar(regions, totals)

ax.set_ylabel('total sales')
ax.set_title('Total video game sales in different regions')
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
def regioncompare(x, y, length, height, idk):

    x_sales = []
    y_sales = []
    idk = pd.DataFrame(idk)
    idk = idk.sort_values(by=[x])
    pd.options.mode.use_inf_as_na = True
    idk = idk.dropna(thresh = 7, axis = 0)


    x_sales = idk[x].tolist()
    y_sales = idk[y].tolist()

    y_backup = y_sales

    x_clean = []
    y_clean = []
    a = 0



    for i in x_sales:
        if i.strip() and y_sales[a].strip():
            y_sales = y_backup
            x_clean.append(float(i))
            y_clean.append(float(y_sales[a]))

        a += 1

    ##old method: use for documentation
    ##x_sales = [i for i in x_sales if i.strip()]
    ##y_sales = [i for i in y_sales if i.strip()]



    ##for row2 in tb:
    ##    if row2[x] != "" and row2[y] != "":
    ##        if row2[x] != "0.0" and row2[y] != "0.0":
    ##            x_sales.append(float(row2[x]))
    ##            y_sales.append(float(row2[y]))


    x1 = np.array(x_clean)
    y1 = np.array(y_clean)

    plt.scatter(x1, y1)
    z = np.polyfit(x1, y1, 2)
    p = np.poly1d(z)
    plt.plot(x1, p(x1))
    plt.axis((0, length, 0, height))
    plt.xlabel(f'{x.capitalize()} Sales')
    plt.ylabel(f'{y.capitalize()} Sales')
    plt.show()

countries = ["other", "japan", "europe", "america"]

for x in countries:
    i = countries.index(x)
    for z in range(i+1, len(countries)):
        print(x, countries[z])
        regioncompare(x, countries[z], round((df[x].max() + 0.5) * 2) / 2, round((df[countries[z]].max() + 0.5) * 2) / 2, tb)



regioncompare("japan", "america", 2.5, 10, tb)
regioncompare("europe", "america", 10, 10, tb)

