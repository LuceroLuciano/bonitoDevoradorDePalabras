"""
conversiones de temperatura

    De Celsius a Kelvin: KELVIN = CELSIUS + 273.15.
    De Celsius a Farenheit: FARENHEIT = (CELSIUS) *9/5 + 32.
    De Farenheit a Celsius: CELSIUS = (FARENHEIT – 32) * (5/9)
    De Farenheit a Kelvin: KELVIN = (FARENHEIT – 32) * (5/9) + 273.15.
    De Kelvin a Celsius: CELSIUS = KELVIN – 273.15.
"""

celsius = 27
farenheit = 80
kelvin = 24

celsius_a_kelvin = celsius + 237.15
celsius_a_farenheit = ((celsius * (9 / 5)) + 32)
farenheit_a_celsius = ((farenheit - 32) * (5 / 9))
farenheit_a_kelvin = (((farenheit - 32) * (5 / 9)) + 237.15)
kelvin_a_celsius = kelvin - 237

print(celsius, "°Celsius equivalen a", round(celsius_a_kelvin, 2), "°Kelvin")
print(celsius, "°Celsius equivalen a", round(celsius_a_farenheit, 2), "°Farenheit")
print(farenheit, "°Farenheit equivalen a", round(farenheit_a_celsius, 2), "°Celsius")
print(farenheit, "°Farenheit equivalen a", round(farenheit_a_kelvin, 2), "°Kelvin")
print(kelvin, "°kelvin equivalen a", round(kelvin_a_celsius, 2), "°Celsius \n")