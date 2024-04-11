#Creating a class for currency that handles both USD and EUR and operation between them (conversion, addition, substraction)

class Currency:
    def __init__(self, amount, currency):
        if currency not in ["USD", "EUR"]:
            raise ValueError("Currency type not valid")
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def conversion(self, other_currency):
        if self.currency == "USD" and other_currency == "EUR":
            return Currency(self.amount * 0.93, "EUR")
        elif self.currency == "EUR" and other_currency == "USD":
            return Currency(self.amount * 1.07, "USD")

    def __add__(self, other):
        if self.currency == other.currency:
            return Currency(self.amount + other.amount, self.currency)
        else:
            print("Different currency types, please conver to same currency and try again")
            return None

    def __sub__(self, other):
        if self.currency == other.currency:
            return Currency(self.amount - other.amount, self.currency)
        else:
            print("Different currency types, please conver to same currency and try again")
            return None


usd1 = Currency(100, "USD")
eur1 = Currency(100, "EUR")

print(usd1)
print(eur1)

usd2 = Currency(70, "USD")
eur2 = Currency(70, "EUR")

print(usd1 + usd2)
print(eur2 + eur1)

print(usd1 + eur1)
print(usd1 - eur1)

usd1_converted = usd1.conversion("EUR")
print(usd1_converted)
print(usd1_converted + eur1)
print(usd1_converted - eur1)