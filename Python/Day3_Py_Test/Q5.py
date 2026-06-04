# Write `convert_temp(value, from_unit, to_unit)` that converts between Celsius, Fahrenheit, and Kelvin. Store each conversion formula as a lambda in a dictionary, look it up and apply it. Test with at least 4 different combinations.

convert_temp = {
    "c2f" : lambda temp: temp * (9 / 5) + 32,
    "f2c" : lambda temp: (temp - 32) * (5 / 9),
    "c2k" : lambda temp: temp + 273.15,
    "k2c" : lambda temp: temp - 273.15,
    "f2k" : lambda temp: (temp -32) * (5 / 9) + 273.15,
    "k2f" : lambda temp: (temp - 273.15) * (9 / 5) + 32
}

print(convert_temp["c2f"](5))
print(convert_temp["f2c"](5))
print(convert_temp["c2k"](5))
print(convert_temp["k2c"](5))
print(convert_temp["f2k"](5))
print(convert_temp["k2f"](5))