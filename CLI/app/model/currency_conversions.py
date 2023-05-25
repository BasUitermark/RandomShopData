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
        'gp': 100,
        'pp': 1000  # 1 pp is 10 gp
    }
    
    # Precision rates
    precision_rates = {
        'cp': 1,
        'sp': 1,
        'gp': 1,
        'pp': 2
    }

    # Start from highest currency and go down
    for currency, rate in reversed(conversion_rates.items()):
        # Check if copper_value can be converted into current currency
        if copper_value >= rate:
            # Check if copper_value is at least 50 gp for pp conversion
            if currency == 'pp' and copper_value < 5000:  # 5000 cp is 50 gp
                continue
            
            precision = precision_rates[currency]
            value = round(copper_value / rate, precision)  # Divide by rate and round to appropriate decimal place

            # Check if the value is an integer and doesn't have a decimal part
            if value.is_integer():
                value = int(value)  # Convert to integer if it's a whole number

            return value, currency

    # If no match found, return in copper pieces
    return round(copper_value, 1), 'cp'