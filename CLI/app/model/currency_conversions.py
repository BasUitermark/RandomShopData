def convert_to_copper(price):
    # Parse price string to extract value and currency type
    value, currency = price.split(' ')
    value = int(value)

    # Conversion rates
    conversion_rates = {
        'cp': 1,
        'sp': 10,
        'ep': 50,
        'gp': 100,
        'pp': 1000
    }
    return value * conversion_rates[currency]

def convert_to_highest_currency(copper_value):
    # Conversion rates
    conversion_rates = {
        'cp': 1,
        'sp': 10,
        'ep': 50,
        'gp': 100,
        'pp': 1000
    }

    # Start from highest currency and go down
    for currency, rate in reversed(list(conversion_rates.items())):
        if copper_value >= rate:
            value = copper_value // rate
            copper_value %= rate
            return f'{value} {currency}'
    # If no match found, return in copper pieces
    return f'{copper_value} cp'