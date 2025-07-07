def celciusToFahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return   fahrenheit
def fahrenheitToCelcius(fahrenheit):
     celsius = (fahrenheit - 32 ) * 5 / 9
     return   celsius
fahrenheit = float(input("Enter fahrenheit: "))
print(fahrenheitToCelcius(fahrenheit))
celsius = float(input("Enter celsius: "))
print(celciusToFahrenheit(celsius))