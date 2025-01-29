import pandas as pd


def is_year_month_separate(df):
    if df["Month"][0].count(" ") > 0:
        return False
    if not df["Month"][0].isalpha():
        return False

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    if df["Month"][0] not in months:
        return False

    return True


print(is_year_month_separate(pd.read_csv("MTM05.20241203T001228.csv")))
print(is_year_month_separate(pd.read_csv("cleaned.csv")))