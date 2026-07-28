print("Temp convertor")
temp = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")

if unit == "C":
    temp = round(1.8 * temp + 32, 2)
    unit = "F"
    print(f"temperature is {temp} {unit}")

elif unit == "F":
    temp = round((temp - 32) / 1.8, 2)
    unit = "C"
    print(f"temperature is {temp} {unit}")

else:
    print(f"{unit} is not a unit")
