# Write a program which prompts the user for a Celsius temperature,
# convert the temperature to Fahrenheit, and print out the
# converted temperature.

celsiusTemp = input('Enter the celsius temperature to convert: ')

fahrenheitTemp = float(celsiusTemp) * (9/5) + 32

print(celsiusTemp, ' degrees celsius is: ', fahrenheitTemp, ' degrees fahrenheit')
