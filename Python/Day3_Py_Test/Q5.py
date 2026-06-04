# Write `convert_temp(value, from_unit, to_unit)` that converts between Celsius, Fahrenheit, and Kelvin. Store each conversion formula as a lambda in a dictionary, look it up and apply it. Test with at least 4 different combinations.

def convert_temp(value, from_unit, to_unit):
    conversions = {
        "c2f" : lambda temp: temp * (9 / 5) + 32,
        "f2c" : lambda temp: (temp - 32) * (5 / 9),
        "c2k" : lambda temp: temp + 273.15,
        "k2c" : lambda temp: temp - 273.15,
        "f2k" : lambda temp: (temp -32) * (5 / 9) + 273.15,
        "k2f" : lambda temp: (temp - 273.15) * (9 / 5) + 32
        }
    key = from_unit + "2" + to_unit
    return conversions[key](value)

print(convert_temp(5, "c", "f"))
print(convert_temp(5, "f", "c"))
print(convert_temp(5, "c", "k"))
print(convert_temp(5, "k", "c"))