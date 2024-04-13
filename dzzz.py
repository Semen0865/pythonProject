class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount):
        return amount / self.exchange_rate

# Припустимо, що ви знаєте поточний курс долара до валюти вашої країни
current_exchange_rate = 39,1676  # Приклад значення, введіть реальне значення курсу

converter = CurrencyConverter(current_exchange_rate)

amount_in_local_currency = float(input("Введіть кількість валюти вашої країни: "))
amount_in_usd = converter.convert_to_usd(amount_in_local_currency)

print(f"Сума в доларах США: {amount_in_usd}")