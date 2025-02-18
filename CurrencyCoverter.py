# Currency Converter
def currency_converter(amount, exchange_rate):
    converted_amount = amount * exchange_rate
    return converted_amount

# Example usage
usd_amount = float(input("Enter amount in USD: "))
exchange_rate_inr = 85  # Example exchange rate (USD to EUR)
inr_amount = currency_converter(usd_amount, exchange_rate_inr)
print(f"{usd_amount} USD is approximately {inr_amount} INR")