
import csv

import matplotlib.pyplot as plt


f = open("MTM05.20241203T001228.csv")
reader = csv.DictReader(f)
tb=[]
for row in reader:
    tb.append(row)

def monthly_mean(tb, place, month):
    total=0.0
    year_count=0

    for row in tb:
        if (row["Meteorological Weather Station"] == place
                and row["Month"].count(month) > 0):
            total += float(row["VALUE"])
            year_count += 1
    return total / year_count



malin_tb = []
for row in tb:
    if (row["Meteorological Weather Station"] == "Malin Head"
            and row["Month"].count("January")):
        malin_tb.append(float(row["VALUE"]))


malin_tb = [monthly_mean(tb, "Malin Head", "January"),
            monthly_mean(tb, "Malin Head", "February"),
            monthly_mean(tb, "Malin Head", "March")]


plt.plot(malin_tb)
plt.show()
