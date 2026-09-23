getInterest = lambda amount,rate,year : (amount * rate * year) / 100
celsiusToFahrenheit = lambda celsius : (celsius * (9/5) + 32)

amount = float(input("Enter Amount: "))
rate = float(input("Enter Rate (%): "))
year = int(input("Enter Year: "))

celsius = float(input("Enter Temperature in Celsius: "))

print(getInterest(amount,rate,year))

print(celsiusToFahrenheit(celsius))

