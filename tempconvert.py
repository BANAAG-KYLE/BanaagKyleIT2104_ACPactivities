def celsius_to_fahrenheit(celsius):
    
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit
    
celsius = float(input("Enter a Celsius valude: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print(f"{celsius:.2f} Celsius is {fahrenheit:.2f} Fahrenheit")
