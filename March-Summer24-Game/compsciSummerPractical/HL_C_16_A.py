# Question 16(a)
# Name: [REDACTED]

def display_intro():
    print("Welcome to my BMI calculator!")


display_intro()

weight = int(input("Enter weight (in kilograms): "))  # read weight
height = int(input("Enter height (in centimeters): "))  # centimeters

bmi = round(weight / (pow(height, 2)) * 10000, 1)

if bmi < 18.5:
    bmi_range = "Underweight"
elif 18.5 <= bmi <= 24.9:
    bmi_range = "Normal"
elif 25 <= bmi <= 29.9:
    bmi_range = "Overweight"
elif 30 <= bmi:
    bmi_range = "Obese"

print("BMI is: ", bmi)
print(bmi_range)
