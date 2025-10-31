import csv
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib.pyplot import figure

f = open("MTM05.20241203T001228.csv", "r")
reader = csv.DictReader(f)
tb = []
for row in reader:
    tb.append(row)


def monthly_mean(tb, place, month):
    total = 0.0
    year_count = 0
    for row in tb:
        if (row["Meteorological Weather Station"] == place
                and row["Month"].count(month) > 0):
            total += float(row["VALUE"])
            year_count += 1
    return total / year_count

malin_tb = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for m in months:
    malin_tb.append(monthly_mean(tb, "Malin Head", m))


# Old matplotlib code
#fig, ax = plt.subplots()
#ax.bar(months, malin_tb)
#plt.show()

# New plotly code
fig = px.bar(title="Average Rainfall", x= months, y=malin_tb)
fig.show()
with open("code.txt", "w") as f:
    f.write(fig.to_html(full_html=False, include_plotlyjs="cdn"))