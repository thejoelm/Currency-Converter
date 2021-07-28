import urllib.request
import json
import decimal


class CurrencyConverter:

    rates = {}

    def __init__(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Currency Bot'})
        data = urllib.request.urlopen(req).read()
        data = json.loads(data.decode('utf-8'))
        self.rates = data["rates"]

    def convert(self, amount, from_currency, to_currency):
        initial_amount = amount
        if from_currency != "EUR":
            amount = amount / self.rates[from_currency]
        if to_currency == "EUR":
            return amount
        else:
            return amount * self.rates[to_currency]

converter = CurrencyConverter("https://api.vatcomply.com/rates")

print("Welcome to the Currency Converter! \nTo access a list of currencies supported, please visit "
                 "https://api.vatcomply.com/rates!")
currFrom = input("Please state the currency you are converting from: ")
currTo = input("Please state the currency you are converting to: ")
strCurrAmount = input("Please state the amount of currency you would like to convert: ")
currAmount = float(strCurrAmount)
convertShort = round(converter.convert(currAmount, currFrom, currTo), 3)

print("The conversion of " + strCurrAmount + " " + currFrom + " to " + currTo + " is " +
      str(convertShort) + " " + currTo)
