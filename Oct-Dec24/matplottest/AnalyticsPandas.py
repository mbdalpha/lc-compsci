import csv
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("MTM05.20241203T001228.csv")

years = []
months = []

for year_month in df["Month"]:
    sepd = year_month.split(" ")
    years.append(sepd[0])
    months.append(sepd[1])

df["Year"] = years
df["Month"] = months

df.to_csv("cleaned.csv")


def monthly_mean(df, place, month):
    filtered_df = df[(df["Meteorological Weather Station"] == place)
                     & (df["Month"] == month)] #potential .isalpha() unit test

    return filtered_df["VALUE"].mean()

means = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for m in months:
    means.append(monthly_mean(df, "Malin Head", m))

plt.plot(means)
plt.show()