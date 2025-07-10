temp = float(input("Enter Temperature:"))

#temperature conversion

unit = input("Enter unit('C' for Celsius or 'F' for Fahrenheit):")

if unit == 'C' or unit == 'c' :
    newTemp = 9/5 * temp - 32
    print("Tempreature in Celsius =",newTemp)
elif unit == 'F' or unit == 'f' :
    newTemp = 5/9 * (temp -32)
    print("Temprature in Fahrenheit =",newTemp)
else :
    print("Unknown unit", unit)