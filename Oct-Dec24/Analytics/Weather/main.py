
import csv

f = open("../../matplottest/.venv/MTM05.20241203T001228.csv")
reader = csv.DictReader(f)
tb=[]
for row in reader:
    tb.append(row)

print(tb)