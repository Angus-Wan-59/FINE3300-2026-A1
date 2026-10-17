class ExchangeRates:
    def __init__(self, file_name):
        #Open the CSV file and only copy the lines into a list
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        #Creating a way to access the relevant lists and regroup the data to prevent reading "," as a string
        header = lines[0].split(",")
        last_row = lines[-1].split(",")

        #Using the position of the name match for FXAUSDCAD in the list to locate the latest exchange rate who shares the same list position in another list and convert it to a float for later calculations
        FXAUSDCAD = header.index("FXAUSDCAD")
        #"self." to make the variable accessible to other methods in the class
        self.latest_rate = float(last_row[FXAUSDCAD])

    #Establishing a method to convert the amount from one currency to another based on information to be input by the user
    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.latest_rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.latest_rate

#Iniating the class just coded above with the desired CSV file
Calculator = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (USD or CAD): ")
to_currency = input("Enter the currency to convert to (USD or CAD): ")

#Calling the convert method from the class to perform the conversion and print the result
result = Calculator.convert(amount, from_currency, to_currency)
print("Your converted amount is now $", round(result, 2), to_currency)